import math
import random
import TermTk as ttk

def hacker(root=None):
    # mainframe = ttk.TTkFrame(parent=root, border=False)
    hboxLay = ttk.TTkHBoxLayout()
    frame = ttk.TTkFrame(parent=root, border=False)
    frame.setLayout(hboxLay)
    binarySolution1 = random.randrange(0, 15, 1)
    binarySolution2 = random.randrange(0, 15, 1)
    binarySolution3 = random.randrange(0, 15, 1)
    binarySolution4 = random.randrange(0, 15, 1)

    class graphTimerEvent():
        def __init__(self, w, type, delay):
            self.timer = ttk.TTkTimer()
            self.val = 10
            self.delay = delay
            self.switch = False
            self.w = w
            self.type = type
            self.timer.timeout.connect(self.timerEvent)
            self.timer.start(1)
        @ttk.pyTTkSlot()
        def timerEvent(self):
            self.switch = not self.switch
            val = [random.uniform(-40,+40)]
            self.val+=1
            self.w.addValue(val)
            self.timer.start(self.delay)

    def demoGraph():
        # frameGraph = ttk.TTkFrame(parent=root, border=False, layout=ttk.TTkGridLayout())
        graphWidget6 = ttk.TTkGraph(color=ttk.TTkColor.fg('#00dd44', modifier=ttk.TTkColorGradient(increment=-30)))
        vboxLay.addWidget(graphWidget6)
        graphTimerEvent(graphWidget6, 6, 0.1)
        # return frameGraph

    # Create a window and attach it to the root (parent=root)
    binariesLayout = ttk.TTkVBoxLayout()

    spin1_1 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin1_2 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin1_3 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin1_4 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    binary1 = ttk.TTkLabel()
    hboxLayBinary1 = ttk.TTkHBoxLayout(parent=binariesLayout)
    hboxLayBinary1.addWidget(spin1_1)
    hboxLayBinary1.addWidget(spin1_2)
    hboxLayBinary1.addWidget(spin1_3)
    hboxLayBinary1.addWidget(spin1_4)
    hboxLayBinary1.addWidget(binary1)
    hboxLayBinary1.addWidget(ttk.TTkLabel(text=binarySolution1))

    spin2_1 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin2_2 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin2_3 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin2_4 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    binary2 = ttk.TTkLabel()
    hboxLayBinary2 = ttk.TTkHBoxLayout(parent=binariesLayout)
    hboxLayBinary2.addWidget(spin2_1)
    hboxLayBinary2.addWidget(spin2_2)
    hboxLayBinary2.addWidget(spin2_3)
    hboxLayBinary2.addWidget(spin2_4)
    hboxLayBinary2.addWidget(binary2)
    hboxLayBinary2.addWidget(ttk.TTkLabel(text=binarySolution2))

    spin3_1 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin3_2 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin3_3 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin3_4 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    binary3 = ttk.TTkLabel()
    hboxLayBinary3= ttk.TTkHBoxLayout(parent=binariesLayout)
    hboxLayBinary3.addWidget(spin3_1)
    hboxLayBinary3.addWidget(spin3_2)
    hboxLayBinary3.addWidget(spin3_3)
    hboxLayBinary3.addWidget(spin3_4)
    hboxLayBinary3.addWidget(binary3)
    hboxLayBinary3.addWidget(ttk.TTkLabel(text=binarySolution3))

    spin4_1 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin4_2 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin4_3 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    spin4_4 = ttk.TTkSpinBox(value=0, maximum=1, minimum=0)
    binary4 = ttk.TTkLabel()
    hboxLayBinary4 = ttk.TTkHBoxLayout(parent=binariesLayout)
    hboxLayBinary4.addWidget(spin4_1)
    hboxLayBinary4.addWidget(spin4_2)
    hboxLayBinary4.addWidget(spin4_3)
    hboxLayBinary4.addWidget(spin4_4)
    hboxLayBinary4.addWidget(binary4)
    hboxLayBinary4.addWidget(ttk.TTkLabel(text=binarySolution4))

    binariesLayout.addItem(hboxLayBinary1)
    binariesLayout.addItem(hboxLayBinary2)
    binariesLayout.addItem(hboxLayBinary3)
    binariesLayout.addItem(hboxLayBinary4)


    # Define the Label and attach it to the window (parent=helloWin)
    hboxLay.addItem(binariesLayout)
    vboxLay = ttk.TTkVBoxLayout(parent=frame)
    hboxLay.addItem(vboxLay, row=0, col=1, rowspan=2)

    progBar = ttk.TTkProgressBar()
    progBar.setMaximumSize(maxw=50,maxh=1)

    vboxLay.addWidget(progBar)
    demoGraph()
    # vboxLay.addWidget(btn)

    spin1_1.valueChanged.connect(lambda x: updateBinary())
    spin1_2.valueChanged.connect(lambda x: updateBinary())
    spin1_3.valueChanged.connect(lambda x: updateBinary())
    spin1_4.valueChanged.connect(lambda x: updateBinary())

    spin2_1.valueChanged.connect(lambda x: updateBinary())
    spin2_2.valueChanged.connect(lambda x: updateBinary())
    spin2_3.valueChanged.connect(lambda x: updateBinary())
    spin2_4.valueChanged.connect(lambda x: updateBinary())

    spin3_1.valueChanged.connect(lambda x: updateBinary())
    spin3_2.valueChanged.connect(lambda x: updateBinary())
    spin3_3.valueChanged.connect(lambda x: updateBinary())
    spin3_4.valueChanged.connect(lambda x: updateBinary())

    spin4_1.valueChanged.connect(lambda x: updateBinary())
    spin4_2.valueChanged.connect(lambda x: updateBinary())
    spin4_3.valueChanged.connect(lambda x: updateBinary())
    spin4_4.valueChanged.connect(lambda x: updateBinary())

    def updateBinary():
        binarystr1 = (
            str(spin1_1.value())
            + str(spin1_2.value())
            + str(spin1_3.value())
            + str(spin1_4.value())
        )
        binary1.setText(int(binarystr1, 2))

        binarystr2 = (
            str(spin2_1.value())
            + str(spin2_2.value())
            + str(spin2_3.value())
            + str(spin2_4.value())
        )
        binary2.setText(int(binarystr2, 2))

        binarystr3 = (
            str(spin3_1.value())
            + str(spin3_2.value())
            + str(spin3_3.value())
            + str(spin3_4.value())
        )
        binary3.setText(int(binarystr3, 2))
        
        binarystr4 = (
            str(spin4_1.value())
            + str(spin4_2.value())
            + str(spin4_3.value())
            + str(spin4_4.value())
        )
        binary4.setText(int(binarystr4, 2))

        updateBar()

    def updateBar():
        tmp = int(
            int(binary1.text()) == binarySolution1) + int(int(binary2.text()) == binarySolution2) + int(int(binary3.text()) == binarySolution3) + (int(int(binary4.text()) == binarySolution4))
        progBar.setValue(tmp/4)
        if int(binary1.text()) == binarySolution1 and int(binary2.text()) == binarySolution2 and int(binary3.text()) == binarySolution3 and int(binary4.text()) == binarySolution4:
            progBar.setValue(1)
            frame.hide()
            successWin = ttk.TTkWindow(parent=root, title="Hacked!", border=True, flags=ttk.TTkK.NONE)
            successWin.addWidget(ttk.TTkLabel(text="You got it all right!"))


def main():
    root = ttk.TTk()
    mainWin = ttk.TTkWindow(parent=root, pos=(1,1), size=(125,20), title="Hack me if you can!", layout=ttk.TTkGridLayout(), flags=ttk.TTkK.NONE)
    hacker(mainWin)
    root.mainloop()

if __name__ == "__main__":
    main()