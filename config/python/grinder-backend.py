#!/usr/bin/python3

import threading
import hal
import linuxcnc
import time
import traceback
from axis import Axis
from grinderhal import GrinderHal
from hal_glib import GStat
from kthread import KThread

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib

class GrinderMotion():
    def __init__(self):
        self.status = linuxcnc.stat()
        self.GSTAT = GStat()
        self.thread = None
        # Initialize HAL and LinuxCNC
        self.initialize_hal()
        self.pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.GSTAT.connect("current-position", self.update_pos)
        self.GSTAT.connect("state-estop", self.stop)
        self.GSTAT.connect("state-off", self.stop)
        self.GSTAT.connect("command-error", self.print_mdi_error)
        self.GSTAT.connect("shutdown", self.shutdown)
        self.GSTAT.connect("error", self.print_error)
        self.is_running = False
    def __del__(self):
        print("GrinderMotion cleaned up")

    def shutdown(self):
        print("Shutdown signal recvd")
        quit()

    def onModeChanged(self):
        running = bool(GrinderHal.get_hal("is_running"))

        if self.is_running != running:
            self.is_running = running
            if running:
                print("Start request BE")
                self.start()
            else:
                print("Stop request BE")
                self.stop()

    def start(self, obj = None):
        if not self.GSTAT.estop_is_clear and not self.GSTAT.machine_is_on and not self.GSTAT.is_all_homed:
            if self.is_running:
                GrinderHal.set_hal("is_running", False)
                self.is_running = False
            return
        
        self.thread = KThread(target = self.main_sequence, name = "MainLoop")
        self.thread.start()
       

    def stop(self, obj = None):
        print("Stopping BE")
        try:
            if self.thread != None:
                self.thread.terminate()
        except threading.ThreadError:
            print("BE thread already stopped")
        
        self.c.abort()
        # self.c.mode(linuxcnc.MODE_MANUAL)
        #self.thread._stop().set()

    def update_pos(self, obj, absolute_pos, relative_pos, dist_to_go, joint_pos):
        self.pos = relative_pos
        self.onModeChanged()

    def get_pos(self, axis):
        return round(self.pos[axis.to_int()], GrinderHal.get_rounding_tolerance())

    def initialize_hal(self):
        self.h = hal.component("grinder")
        self.c = linuxcnc.command()

        self.h.newpin("x_min", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("x_max", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("y_min", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("y_max", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("z_min", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("z_max", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("x_speed", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("y_speed", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("z_speed", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("z_direction", hal.HAL_BIT, hal.HAL_IO)
        self.h.newpin("z_crossfeed", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("y_downfeed", hal.HAL_FLOAT, hal.HAL_IN)
        self.h.newpin("enable_x", hal.HAL_BIT, hal.HAL_IO)
        self.h.newpin("enable_y", hal.HAL_BIT, hal.HAL_IO)
        self.h.newpin("enable_z", hal.HAL_BIT, hal.HAL_IO)
        self.h.newpin("stop_at_z_limit", hal.HAL_BIT, hal.HAL_IN)
        self.h.newpin("crossfeed_at", hal.HAL_S32, hal.HAL_IN)
        self.h.newpin("repeat_at", hal.HAL_S32, hal.HAL_IN)
        self.h.newpin("is_running", hal.HAL_BIT, hal.HAL_IO)
        
        self.h.ready()

        print("Grinder hal ready")

        #hal.new_sig("grinder.z_direction", hal.HAL_BIT)

        hal.set_p("grinder.z_direction", str(1))

        hal.set_p("grinder.x_min", str(0.0))
        hal.set_p("grinder.x_max", str(0.0))
        hal.set_p("grinder.y_min", str(0.0))
        hal.set_p("grinder.y_max", str(0.0))
        hal.set_p("grinder.z_min", str(0.0))
        hal.set_p("grinder.z_max", str(0.0))

        hal.set_p("grinder.x_speed", str(0.0))
        hal.set_p("grinder.y_speed", str(0.0))
        hal.set_p("grinder.z_speed", str(0.0))

        hal.set_p("grinder.z_crossfeed", str(0.0))
        hal.set_p("grinder.y_downfeed", str(0.0))

        # Enable and control signals
        hal.set_p("grinder.enable_x", str(False))
        hal.set_p("grinder.enable_y", str(False))
        hal.set_p("grinder.enable_z", str(False))
        hal.set_p("grinder.stop_at_z_limit", str(False))

        # Crossfeed and repeat settings
        hal.set_p("grinder.crossfeed_at", str(0))
        hal.set_p("grinder.repeat_at", str(0))

        hal.set_p("grinder.is_running", str(False))
    # Main logic sequence

    def print_mode(self):
        
        self.status.poll()
        if self.status.task_mode == linuxcnc.MODE_MANUAL:
            print("Current mode: Manual")
        elif self.status.task_mode == linuxcnc.MODE_AUTO:
            print("Current mode: Auto")
        elif self.status.task_mode == linuxcnc.MODE_MDI:
            print("Current mode: MDI")


    def print_error(self, error):
        print(f"Linuxcnc error returned: {error}")

    def print_mdi_error(self, thing):
            self.c.abort()
            GrinderHal.set_hal("is_running", False)
            self.c.mode(linuxcnc.MODE_MANUAL)
            self.c.wait_complete()
            self.status.poll()

            e = linuxcnc.error_channel()
            error = e.poll()

            if error:
                kind, text = error
                if kind in (linuxcnc.NML_ERROR, linuxcnc.OPERATOR_ERROR):
                    typus = "error"
                else:
                    typus = "info"
                print(typus, text)
            
    def get_max_wait(self):
        # x_max = float(GrinderHal.get_hal("x_max"))
        # x_min = float(GrinderHal.get_hal("x_min"))
        # x_speed = float(GrinderHal.get_hal("x_speed"))
        # y_max = float(GrinderHal.get_hal("y_max"))
        # y_min = float(GrinderHal.get_hal("y_min"))
        # y_speed = float(GrinderHal.get_hal("y_speed"))
        # z_max = float(GrinderHal.get_hal("z_max"))
        # z_min = float(GrinderHal.get_hal("z_min"))
        # z_speed = float(GrinderHal.get_hal("z_speed"))

        # x_dist = abs(x_max - x_min)
        # x_time_sec = x_dist/x_speed/60
        # y_dist = abs(y_max - y_min)
        # y_time_sec = y_dist/y_speed/60
        # z_dist = abs(z_max - z_min)
        # z_time_sec = z_dist/z_speed/60

        return 30 #max(x_time_sec, max(y_time_sec, z_time_sec))

    def main_sequence(self):
        print("Started")

        self.c.mode(linuxcnc.MODE_MDI)
        self.c.wait_complete()

        x_pos = self.get_pos(Axis.X)
        x_max = float(GrinderHal.get_hal("x_max"))
        x_min = float(GrinderHal.get_hal("x_min"))
        y_pos = self.get_pos(Axis.Y)
        y_max = float(GrinderHal.get_hal("y_max"))
        y_min = float(GrinderHal.get_hal("y_min"))
        z_pos = self.get_pos(Axis.Z)
        z_max = float(GrinderHal.get_hal("z_max"))
        z_min = float(GrinderHal.get_hal("z_min"))

        if x_pos > x_max + 0.00001 and bool(GrinderHal.get_hal("enable_x")):
            mdi = f"G0 X{x_max}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())

        if y_pos > y_max + 0.00001 and bool(GrinderHal.get_hal("enable_y")):
            mdi = f"G0 Y{y_max}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())

        if z_pos > z_max + 0.00001 and bool(GrinderHal.get_hal("enable_z")):
            mdi = f"G0 Z{z_max}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())

        if x_pos < x_min - 0.00001 and bool(GrinderHal.get_hal("enable_x")):
            mdi = f"G0 X{x_min}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())

        if y_pos < y_min - 0.00001 and bool(GrinderHal.get_hal("enable_y")):
            mdi = f"G0 Y{y_min}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())

        if z_pos < z_min - 0.00001 and bool(GrinderHal.get_hal("enable_z")):
            mdi = f"G0 Z{z_min}"
            self.c.mdi(mdi)
            self.c.wait_complete(self.get_max_wait())
        
        while True:
            # the thread will be terminated by the outside process, but just in case this can stop it faster:
            if not self.is_running:
                
                self.c.abort()
                self.c.wait_complete()
                print("Stopped")
                # return
            else:
                print("Loop")

                self.c.mode(linuxcnc.MODE_MDI)
                self.c.wait_complete()
                # self.c.mdi("G1 X1 F1000")
                # self.c.wait_complete()
                # self.c.mdi("G1 X0 F1000")
                self.c.mdi("o<xmove_to_max> call")
                self.c.wait_complete(self.get_max_wait())
                self.c.mdi("o<xmove_to_min> call")
                self.c.wait_complete(self.get_max_wait())

                print("End Loop")
                
                time.sleep(0.005)

# Run the main sequence
#try:
grinderBackend = GrinderMotion()
print("GRINDER_BACKEND STARTED")
GLib.MainLoop().run()
# except KeyboardInterrupt:
#     print("Motion controller stopped.")
#     # GLib.MainLoop().stop()
#     raise SystemExit

