# circletosquare
This program converts a set of circle coordinates (coordinates underneath the line of a circle with a given radius), into a transformed set of coordinates based on a square with the same diameter (in the shown example with a radius of 256; -256 <= x <= 256, -256 <= y <= 256). 
![image](https://github.com/user-attachments/assets/319a916e-778a-42ba-b127-6295ca7e0d90)


into

![image](https://github.com/user-attachments/assets/c2aacef0-a04f-4693-b1ab-e1921729197c)

But, I wanted it to not just work at the edges, and to transform any coordinate according to the transformation of the circle into the square. So, for example:

![image](https://github.com/user-attachments/assets/22729cd1-938f-40d9-a6b7-b992bd3f940b)


Etc. The purpose of this was to see how I would convert a joystick which has the wrong maximum inputs, as a circle, and map them onto correct maximum inputs, as a square. The actual file only has a radius of 1, as that matches with windows' measurement of a controller's input.
