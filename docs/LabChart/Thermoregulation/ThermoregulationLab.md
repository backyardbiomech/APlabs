# Physiology Lab – Heat and Insulation

## Lab objectives:

The goal of this lab exercise is to gain a practical understanding of the factors that influence heat loss and gain in animals as well as their relative importance.

## Scientific background: 
Your textbook has an entire chapter on temperature regulation in animals.  While you will need to read this entire chapter for the lecture class, you should focus for the lab on the section dealing with the physics of heat transfer.  Additionally, the material below offers a summary of some of the basic physics of heat transfer in animals, and how we may separate the different effects in lab. 

### Overview
In this lab we will use a *model* of an organism to investigate biologically relevant aspects of heat transfer. Your model organism in this case is the “mouse”, a small cylinder of aluminum with a heat capacity and surface area *similar* to those of a very small mammal, such as a mouse or rat. However, unlike an endothermic mammal, this model does not continue to produce internal heat.

You will be comparing different mice and different circumstances to measure the relative importance of the factors that influence heat loss in animals and to estimate the amount of energy your mouse would need to expend to stay warm in these conditions.

Your textbook lists four factors that lead to heat loss or gain in animals (or any other object) – conduction, convection, radiation and evaporation.  

The first of these, **conduction**, transfers heat down a gradient. Consider a warm mouse sitting in relatively chilly air. Heat is conducted away from the mouse into the layer of air molecules in contact with the surface of the mouse. These molecules of air will then warm the air a bit further away from the mouse and so on. The rate at which the mouse loses heat by conduction can be calculated as $\dot{Q}$ using the equation below. 

Heat loss by conduction: 
$$\dot{Q} = kS\frac{T_2-T_1}{l}$$

where $S$ is the surface area of the animal, an easy thing to measure on the cylindrical model, and $k$ is the thermal conductivity of the insulator – air in this case ($0.024\ Wm^{-1}K^{-1}$ for 25°C air). The temperatures $T_2$ and $T_1$ are two temperatures at some distance $l$ from each other. We could assume that $T_1$ is the temperature of the mouse and that $T_2$ is the temperature of the air at some location, but which location should we use?  $T_1$, $T_2$ and $l$ are meant to reflect a temperature difference across some insulator – maybe a layer of fur – but what should we do when air itself is the insulator?  If we assume that the thickness of insulation is very small – perhaps the distance from the mouse to the first molecule of air, then the calculated heat flux would be very large (due to dividing by a very small $l$).  Of course, in this case the air molecule would quickly heat up, destroying the temperature gradient (the two temps would be equal), making our calculation meaningless.  If instead we assume that $T_2$ is some distance far away from the mouse – perhaps across the room – then the intervening air will not change in temperature, but our calculated heat flux would be ridiculously small.  The most appropriate option is to assume that $T_2$ is “ambient air temperature” and that $l$ is the thickness of the **boundary layer** (see below in Terms & Equations) of air around the mouse.  Boundary layers are often difficult to measure exactly, but for a mouse sitting in (relatively) still air, we will assume that the boundary layer is approximately $0.4\ cm$ thick, allowing us to calculate a reasonable heat flow from the mouse due to conduction into the air.

Should we next worry about the outside of the mouse cooling down faster than the inside of the mouse, leading to temperature gradients within the mouse?  These gradients do affect calculations of heat flux in animals, but we do not need to worry in this case.  The thermal conductivity ($k$) of our aluminum mouse ($205\ Wm^{-1}K^{-1}$) is very high compared to that of muscle and fat ($<1\ Wm^{-1}K^{-1}$), let alone air or fur, so heat will flow much more rapidly within the mouse than outside the mouse. In other words, all parts of the mouse model will stay at a uniform temperature, unlike an actual animal in which the core is generally warmer than the surface.

As the above paragraphs show, the rate of conductive heat loss for animals in fluids such as air or water is fundamentally affected by the **boundary layer** around the animal.  This brings us to the next question and the next factor discussed in your textbook – **convection** – heat transfer by movement of fluid.  What if something thinned or reduced the boundary layer around an animal, bringing “room temperature” air closer to it?  This would clearly increase **conductive** heat flow into the fluid by reducing length $l$, increasing the temperature difference $T_1-T_2$, or both. Many factors can reduce the thickness of a boundary layer.  Bulk motion of the fluid such as wind or a water current can thin the boundary layer.  For example, a gentle breeze of $1\ ms^{-1}$ (equal to $2.2\ mi.\ hr^{-1}$) thins the boundary layer around your mouse from approximately $0.4\ cm$ to $0.1\ cm$. Reduction of boundary layer thickness due to external fluid motion is known as **forced convection**.  However, convection need not be forced – it occurs in many cases simply because fluids change density with changes in temperature, leading to motion.  For example, the warm air in the boundary layer next to the mouse is less dense than the cooler surrounding air. That lower density makes the warmer air rise, which then draws new cool air in towards the animal.  This type of convection is termed **natural convection** and is nearly impossible to avoid in an experiment such as the one we’ll perform in lab.  **Convection** is also difficult to model or predict with a simple equation such as the one used above for conduction, since it requires an understanding of fluid flow, which may depend a great deal on shape and orientation.  However, the effects of convection can easily be uncovered by experiments on our mouse.  Lastly, remember that convection is fundamentally linked to conduction, because of the disruption of the insulating boundary layer.

Heat transfer by **radiation** is perhaps the least intuitive of the factors influencing heat balance in organisms.  Animals both **absorb** heat by radiation from a source such as the sun or the surroundings and **emit** by radiation into their environment.  The extent to which both occur depends on specific properties of each material and their temperatures.  The wavelength of radiation emitted by an object depends on its temperature; the hotter the object, the shorter the wavelength of the radiation it emits.  For instance, molten iron is hot enough to glow – emitting radiation in the *visible spectrum*.  Typical mammalian body temperatures are such that emitted radiation is in the mid-infra-red wavelengths; invisible to the naked eye but detectable with the appropriate type of camera or sensor.  The amount of radiation emitted or absorbed by an animal depends on its temperature, but also the **emissivity** or **absorptivity**; a sort of analogue to conductance.  Like conductance, emissivity and absorptivity are essentially bi-directional.  An animal with low conductance (good insulation) both loses and gains heat slowly; *an animal with high emissivity necessarily also has an equally high absorptivity*.  Additionally, emissivity and absorptivity are specific to wavelength.  As you may have experienced, a white cotton shirt is less absorptive than a black shirt in the visual spectrum (where much of the radiant energy from the sun lies), but both are about equally absorptive and emissive in the infra-red spectrum where mammals radiate heat. Our aluminum mice come in two phenotypes – one polished, reflective and with a low absorptivity in all wavelengths; the other is flat black with high absorptivity at all wavelengths.

The last heat transfer mode discussed by your textbook is **evaporation**. Essentially, evaporation is using the high heat of vaporization of water to cool the animal.  Vaporization takes energy (in the form of heat) from the animal and imparts it to the water, shifting the water from the liquid phase to the gas phase.  Your textbook notes that about 580 calories (0.580 Calories or kilocalories) is usually used as the standard rate of heat loss due to evaporation of a **gram of water**.  In certain cases, phase changes in water can lead to heat gain.  Any condition that causes water vapor to condense on the skin of the animal lead to heat gain.  You may have experienced this yourself in the summer when stepping out of an air-conditioned building into a hot day with 100% relative humidity. High humidity makes the air feel hotter than it is because it reduced evaporation heat loss, and in extreme changes, can literally add heat to your skin. 

Calculation of the amount of heat transferred by evaporation is simple, since all that is required is a measure of how much water underwent a phase change.  It is not necessary to know the area over which the evaporation occurred, although area can influence the rate at which evaporation occurs.  

Our model aluminum mice cannot sweat or otherwise intentionally evaporatively cool themselves, but we can mimic natural evaporative cooling by gently wetting the mouse with cool or  warm water.

The above equations are not quite sufficient to analyze the data you’ll gather during lab.  Firstly, all of them are in terms of heat flow, not the animal’s actual change in temperature in response to that heat flow.  Thus, while the equations do tell us how much heat an animal would need to produce or lose to maintain a constant temperature, they won’t be of immediate help in our experiments where we record the **temperature changes** of our “mouse” in different conditions.  To go further, we need to know the **heat capacity** of the mouse, or how much heat (energy, in *Joules* or *calories*) needs to be added or removed to change its temperature by 1°C.  The heat capacity of an object is a function of its **volume** and the **materials** it is made of.  To account for the volume, we can find the heat capacity *per cubic cm*; one cubic cm of water has a mass of 1 g. Our aluminum “mice” have a volumetric heat capacity of about  $2.4\ Jcm^{-1}°C^{-1}$. That means it takes 2.4 joules (about 1/2 a calorie) to heat up a 1 cm x 1 cm x 1 cm of aluminum from 25 °C to 26 °C. For comparison, whole-body animal heat capacity (it varies by tissue) is about $2.9\ Jcm^{-1}°C^{-1}$. By this, it would take a flux of roughly 10-14 calories (depending on size) to change a typical small mouse's body temperature by 1 °C. We can convert our **heat** flow rates, ($\dot{Q}$), into rates of **temperature** change ($\dot{T}$) by dividing heat flow by heat capacity.

Additionally, many of the heat flow equations predict exponential decay of the difference in temperatures between the two objects (or between the object and environment). In other words, as the temperature gradient gets smaller, the heat flow rate gets smaller, so heat flow is not linear over time. This provides an easy way to measure some of these parameters – you can measure the **half-life of the curve** instead of trying to fit an equation to all of the data.  However, we might not want to wait for long enough for a complete half-life to occur (i.e. for the temperature *difference* to decrease by one half). Instead, you can use this equation to calculate a half-life from any two points on the curve:

$$t_{1/2} = \frac{\Delta{t}\log{(\frac{1}{2})}}{\log{(\frac{T_2-T_A}{T_1-T_A})}}$$

where $\Delta{t}$ is the time difference in seconds between the two measurements, $T_1$ is the first temperature measurement, $T_2$ the second temperature measurement, and $T_A$ is the ambient (environmental) temperature that the animal is cooling (or heating) toward. $Log$ can be either the natural or base 10 logarithm as long as you use the same form in both places.

For example, let’s say that the mouse’s initial temperature is 43.7 °C, and its temperature *2 minutes later* is 40.2 °C.  Room temperature is known to be 23.2 °C.  Therefore we measure half-life as:

$$t_{1/2} = \frac{120\log{(\frac{1}{2})}}{\log{(\frac{40.2-23.2}{43.7-23.2})}} = 444\ s$$

In other words, with an original temperature gradient of $43.7 - 23.2 = 20.5 °C$, it would take 444 seconds (7.4 minutes) for that difference to halve to 10.25 °C, at which point the mouse temperature would be $23.2 + 10.25 = 33.45 °C$.

#### Terminology and Equations

**Rate of heat transfer by conduction**: 
$$\dot{Q} = kS\frac{T_2-T_1}{l}$$

+ $\dot{Q}$ = rate of heat transfer ($Js^{-1}$)
+ $k$ = thermal conductivity ($Js^{-1}m^{-1}°C^{-1}$)
+ $S$ = surface area ($m^2$)
+ $T_2$ & $T_1$ = temperature samples (°C) 
+ $l$ = distance between the two temperature samples ($m$)

**Boundary Layer** – the layer of fluid around a solid object that moves with the object instead of with the rest of the fluid
Lab tips:

1. Try to keep your mouse from swinging on its string as this leads to additional airflow (convection) past it.
2. Always record an ambient temperature with your probe, then insert it into your mouse while recording and add a comment to note the insertion. Wait at least 10 seconds after that comment before taking measurements.

### Lab Procedure:

#### Overview:
In each of these experiments you will:

+ pull a “mouse” from the warm water bath
+ dry it thoroughly (except for one)
+ suspend the mouse from your ring stand
+ start recording
+ record ambient temperature
+ insert the temperature probe and add a comment
+ begin a treatment while recording the mouse’s temperature for at least five minutes, sometimes longer
+ when complete, take the measurements needed to calculate the surface area of the mouse

Throughout, you should take good notes to keep track of what you did and any measurements.

The temperature probe is a small, white waterproof wire which plugs into port 1 on the PowerLab. 

For each experiment, you want to open the `Thermoregulation Settings` file in LabChart.

#### Experiment 1 – “Natural convection”
In this experiment we will estimate the effect of natural convection on the effective thickness of the boundary layer around a naked silver “mouse” cooling off in room air.


1. Open a clean recording session in LabChart with the `Thermoregulation Settings` file. 
2. Fish a shiny “mouse” out of the water bath and dry it off with a towel.
3. Hang the mouse by the string from the ring-stand.
4. Hold the temperature probe by the wire several inches back from the end, holding the end up in the air away from you and the mouse.
5. Click `Start` to start recording.
6. After several seconds of recording the air temperature, insert the probe to the center of the mouse, add a comment like `probe inserted` to the recording, and move your hands away. 
7. Do not move around the mouse - this will increase air flow and increase convection.
8. You should immediately see the temperature rise, but after a few moments it should begin to slowly decline, and continue to decline consistently for the full time of the recording.
   1. If it goes back up and down, the probe may have moved, or someone disturbed the air around the mouse. Start again with a fresh mouse.
9. Continue recording for **5 minutes** while trying to avoid any disturbances to the air around the mouse.
10. After 5 minutes, stop recording and save your data using a meaningful name. I recommend `LastName_NaturalConvection.adicht`.
11. Share that file with yourself (USB stick, email, etc). You can extract the rest of the data in the [free LabChart Reader](https://www.adinstruments.com/support/software) on your personal computer. 
12. Take the measurements needed to calculate the surface area of the mouse

##### Data Analysis
1. Open the data file in `LabChart Reader` (or `LabChart` on a lab computer if there is time)
2. Open a DataPad viewer. Confirm or set up the following:
   1. Click below column label `A`, click on `Selection & Active Point`, and select `Selection Start`. 
   2. At the top of that dialog, click on the right arrow to change to `column B`, and set it to `Selection End`.
   3. Go to `column C` and and in `Selection and Active Point` choose `Value`, and make sure that under `Calculation Source` that the source channel is set to `Ch 1 Temperature`.
   4. Go to `column D`, select `Statistics`,  `End Value - Start Value`, and make sure that under `Calculation Source` that the source channel is set to `Ch 1 Temperature`.
   5. Go to `column E`, select `Statistics`, `mean`, and make sure that under `Calculation Source` that the source channel is set to `Ch 1 Temperature`.
3. Use your cursor to select a few seconds of the ambient temperature recording. **Add to DataPad**
4. Now select from about **1 minute after the peak temp** to about 1.5 minutes after peak temp (so select about 30 s of the graph, you don't have to be exact). **Add to DataPad**.
    1. Repeat these 30 second selections and add to DataPad for selections starting at 2, 3, and 4 minutes after the peak.
    2. If you think you messed up, it's best to select all the rows in the DataPad, delete the data, and start selecting and adding again.
5. View the DataPad. For each selection you will see the start and end times, the start temperature, the change in temperature, and the mean temperature during that selection (we'll only use this for ambient)
6. Open the thermoregulation data worksheet in Excel.
7. In DataPad, select the first row (that was the ambient temperature), copy, and paste it into the correct place in Excel.
8. Copy the four rows representing the four 30 s selections, and paste into the proper place in Excel.
9. Use Excel formulas to calculate the end temperature for each of the 30 s intervals, then calculate half-life by converting the equations above into Excel formulas.
10. Your value for half-life should be between 200 and 800 seconds. If it is not, consider possible sources of error and check your data.

#### Experiment 2 – “Forced convection”
Everything here is basically the same as the last experiment in terms of measurement procedures. Now, however, we’ll fan the “mouse” using a folded piece of paper to see just how much faster forced convection cools the animal, as measured by the half-life.  

1. Get a new warm shiny mouse from the tank. Dry it off with a towel.
2. Hang the mouse from the ring-stand, start recording data  while holding the temperature probe by the wire in mid-air.  Collect data for a few seconds to get a measurement of ambient air temperature.
3. Insert the temperature probe into the center of “mouse”, add a comment like `probe inserted` to the recording, move your hands away, and continue recording. Begin gently fanning the mouse at a steady rate. Keep it up for at least 5 minutes.
4. After 5 minutes, stop recording and save the data with a meaningful name. Share the data with yourself for analysis on your own computer.
5. Take the measurements needed to calculate the surface area of the mouse
6. Use the same DataPad process as above, select and save ranges of data. Copy, and paste into the appropriate places in the Excel file, then compute the four measurements of half-life under conditions of `forced convection`.

#### Experiment 3 – “Radiant heat gain and loss”
Next we’ll use mouse color phenotypes – the shiny type and the flat black type to examine how absorptivity and emissivity influence thermoregulation.

1. Get a desk lamp and plug it in. Position it so that you will be able to get the bulb about 10 cm from a hanging mouse.
2. Get a flat black mouse from the tank. Dry it off with a towel.
3. Hang the mouse from the ring-stand and start recording data while holding the temperature probe by the wire in mid-air. Collect data for a few seconds to get a measurement of room air temperature.
4. Turn on your desk lamp and point it at the mouse.  Position the bulb about 10 cm away from the side of the mouse (not the end, and definitely not the wire).
5. Insert the temperature probe into the “mouse”, add a comment like `probe inserted` to the recording, move your hands away, and continue recording for 5 minutes. **DO NOT STOP THE RECORDING!
6. Turn off your desk lamp. Insert a comment of `light off` in LabChart.
7. Allow recording to continue for another 5 minutes with the light off, then stop it and save the data file with a meaningful name.
8. Perform steps 1-7 using a shiny mouse. Share both files with yourself for analysis on another computer.
9. Take the measurements needed to calculate the surface area of the mouse.
10. Using the same DataPad process as above, select and save ranges of data. Copy, and paste into the appropriate places in the Excel file, then compute the four measurements of half-life under conditions of `radiant heat gain and loss`.

#### Experiment 4 – “Evaporative heat loss” Optional if sufficient time
Our mouse should cool down much more rapidly if it uses evaporative cooling.  We’ll mimic mouse sweating (or panting) by giving the mouse a wet coat to hold liquid water next to its body and let it evaporate.

1. Get a shiny mouse from the tank. DON'T dry it off. Instead, while its wet, wrap it with a single layer of Kimwipes (cut to size). Ensure the paper is fully wet. Add some drops from the water bath if necessary.
2. Hang the mouse from the ring-stand and begin recording data while holding the temperature probe by the wire in mid-air.  Collect data for a few seconds to get a measurement of room air temperature.
4. Insert the temperature probe into the “mouse” and continue recording, add a comment like `probe inserted` to the recording, and move your hands away. You should immediately see the temperature rise, but after a few moments it should begin to slowly decline.
5. Record for 5 minutes, the stop. Save your data file with a meaningful name.
6. Share the file with yourself for analysis on another computer.
7. Take the measurements needed to calculate the surface area of the mouse.
8. Using the same DataPad process as above, select and save ranges of data. Copy, and paste into the appropriate places in the Excel file, then compute the four measurements of half-life under conditions of `evaporative heat loss`.


#### Experiment 5 – “Fleecy mouse” Optional if time permits
Our model mice are unlike most organisms in that they lack any form of insulation, fur or otherwise.  Here we’ll mimic the effect of one of the better biological insulators by wrapping our mouse in a small blanket.

1. Get a shiny mouse from the tank. Dry it off with a towel. Wrap it in a piece of cloth towel or fleece, held on with a rubber band.
2. Hang the mouse from the ring-stand and begin recording data while holding the temperature probe by the wire in mid-air.  Collect data for a few seconds to get a measurement of room air temperature.
3. Insert the temperature probe into the “mouse” and continue recording, add a comment like `probe inserted` to the recording, and move your hands away. You should immediately see the temperature rise, but after a few moments it should begin to slowly decline.
4. Record for 5 minutes, the stop. Save your data file with a meaningful name.
5. Share the file with yourself for analysis on another computer.
6. Take the measurements needed to calculate the surface area of the mouse
7. Using the same DataPad process as above, select and save ranges of data. Copy, and paste into the appropriate places in the Excel file, then compute the four measurements of half-life under conditions of `insulation`.


### Data analysis & calculations

Your lab notebook questions ask you to make several calculations. In addition to the formula above, the following will be helpful; some algebra skills will also be helpful.

Your calculations in the Excel sheet calculated the temperature half life based on the **data**, but note that to do those calculations you didn't have to use conductivity, heat capacity, surface area, or anything else. 

There are other formula that you could use, if you knew the specific measurements, to **predict** half life. For example, to predict the half-life of cooling due to conductive heat loss:

$$t_{1/2} = \frac{\ln{(2)}c_pl}{kS}$$

where $S$ is the animal’s surface area, $c_p$ is the animal’s heat capacity (see above), $\ln{(2)}$ is the natural logarithm of 2, $k$ is the conductivity of the insulator and $l$ is the thickness of the boundary layer.

In cases where radiant heat loss is also important, half-life can be approximated by:

$$t_{1/2} = \frac{\ln{(2)}c_pl}{kS}-\ln{(2)}C$$

where $C$ is a lumped term representing emissivity, surface area and Stefan-Boltzmann’s constant.