# coding: utf-8
from PySide2.QtCore import QObject, Signal


class SignalBus(QObject):
    """ Signal bus """

    switchToSampleCard = Signal(str, int)
    micaEnableChanged = Signal(bool)
    toggleThemeSignal = Signal()
    supportSignal = Signal()


signalBus = SignalBus()