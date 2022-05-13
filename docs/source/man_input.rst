Input
=====

Input allows the user to interact with the game using input devices.

IGE supports many types of inputs, including:

   * Touch Screen
   * Mouse
   * Keyboard
   * *(WIP)* Motion Sensors: Accelerometor, Gyroscope
   * *(WIP)* Joystick 
   * *(WIP)* Controller



Using Touch Screen
------------------

The Input module is a Python module which provides functions to work with input devices.

To simplify the implementation, the Touch Screen and Mouse inputs are implemented in ``igeCore.input.touch`` module. We support multiple touch by default.

Mouse events are map to touch, with special finger Id for left, right and middle buttons.

Below is an example of how to use Touch to control UI behavior:

.. code:: python

   from igeScene import Script
   from igeCore.input.touch import Touch

   class TouchTest(Script):
      def __init__(self, owner):
         super().__init__(owner)

      def onUpdate(self, dt):
         if Touch.count() > 0:
            for i in range(0, Touch.count())
               x,y = Touch.getPosition(i)
               if Touch.isPressed(i):
                  print(f"Pressed {Touch.getId(i)} at ({x}, {y})")

Using Keyboard
--------------

To get access to Keyboard, use the ``igeCore.input.keyboard`` API.

Below is an example of how to use keyboard:

.. code:: python

   from igeScene import Script
   from igeCore.input.keyboard import KeyCode, Keyboard

   class KeyboardTest(Script):
      def __init__(self, owner):
         super().__init__(owner)

      def onUpdate(self, dt):
         if Keyboard.isPressed(KeyCode.KEY_SPACE):
            print("SPACE pressed - FIRE")

Using Virtual Keyboard
----------------------

Use the API below to show/hide virtual keyboard.

.. code:: python

   from igeScene import Script
   import igeCore
   from igeCore.input.keyboard import KeyCode, Keyboard

   class VirtualKeyboardTest(Script):
      def __init__(self, owner):
         super().__init__(owner)

      def onUpdate(self, dt):
         if not igeCore.isVirtualKeyboardShown(): # check if VK is show
            igeCore.showVirtualKeyboard("Input default text here...") # request show VK

         if Keyboard.isPressed(KeyCode.KEY_RETURN):
            text = igeCore.getInputText() # get the text
            igeCore.hideVirtualKeyboard() # hide the keyboard
