"""Leader modules for teleoperation input devices."""

from .arm_reader import LeaderArmReader as LeaderArmReader, main as leader_arm_main
from .joycon_reader import JoyConReader as JoyConReader, main as joycon_main

__all__ = [
    "LeaderArmReader",
    "leader_arm_main",
    "JoyConReader",
    "joycon_main",
]

# paddle_leader pulls in the optional VR stack (dexstream), absent on exo/JoyCon-only
# hosts (e.g. the Jetson). Guard it so `import omniteleop.leader` still works without
# VR. Match on the top-level package name (exc.name is "dexstream.retargeting", not
# "dexstream"). See vega_module/.docs/CODE_PATCHES.md.
try:
    from .paddle_leader import PaddleLeader as PaddleLeader, main as paddle_main
except ModuleNotFoundError as exc:
    if (exc.name or "").split(".")[0] != "dexstream":
        raise
else:
    __all__ += ["PaddleLeader", "paddle_main"]

