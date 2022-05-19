# GifIndustry-pixel
Gif maker for mindustry.


This program allows you to generate code for mindustry cores for printing gif images into display.


# User manual:

Let's figure out what we can see in this interface.
Here is some settings for making gifs, and some control buttons.


Settings description:

- CoreCount - count of drawing cores. Increasing this setting allows you to draw larger gifs.
- PixelScale - scale of one pixel of result. All images are pre-resized to 176x176 and after that this setting is used. Increasing this setting allows you to draw larger gifs.
- BitForColor - count of bits which will be used for encode each image color (from 1 to 8). Reducing this setting allows you to draw large gifs.
- FPS - frames per second (from 1 to 1000). Reducing this setting decreases the lag count.
- MemCells - number of processor groups. See the connection guide after UI description for more info. Increasing this setting decreases the lag count.


Buttons description:

- Select GIF - allows you to choose gif for work.
- Run - is enabled after all settings and gif choosen. Starting the generation algorithm. May stop the app, but it's ok, you just need to wait. Progress bar is coming soon.
- Save - is enabled after using Run button. Saves the code for cores in chosen directory.
- Prev - allows you to see the previous frame. (hot key - "A")
- Next - allows you to see the next frame. (hot key - "D")
- Buttons Play and Stop are coming soon.

![image](https://user-images.githubusercontent.com/54832404/169388965-b78db900-2fee-44d4-bb68-59e6e9cb5d54.png)


# Connection guide:

After you save the code for cores you may find the files like "01.txt" - "\<n\>.txt" and "overmind.txt". Let's figure out what to do with them and how to connect cores.


Correct scheme may have "overmind core", "drawing cores" splitted into \<MemCells\> groups, <MemCells> memory cells for comunication between "overmind core" and "drawing cores" and display.


- "Overmind core" is used for choose which frame should be drawn into display. It must  be filled by file "overmind.txt".
- "Drawing cores" takes the frame nuber from current memory cell and draw that frame. If \<MemCells\> > 1 then "drawing cores" will work group by group, which decrease the display buffer owerflow chanse. They must  be filled by files from "01.txt" to "\<n\>.txt".

Correct connection you can see in image below.
![image](https://user-images.githubusercontent.com/54832404/169396447-15fd97b0-ae58-4402-ab60-021eabb0a843.png)


# Result
![image](https://user-images.githubusercontent.com/54832404/169397381-559278fc-95ef-4d3d-8456-962ce02a6498.png)
