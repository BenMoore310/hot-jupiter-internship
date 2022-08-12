# How to use my scripts


Most of these scripts can just be run and as long as the file paths are correct they should create the right graphs/outputs.

Daily checks scripts:

Zonal-mean zonal wind: in the "winds" folder, the winds_general and winds_general_kinetic scripts create the zonal wind plots for the eq and kinetic runs, all you have to change is the values of the timesteps it iterates over when it loops through them all.

check_energy does the plot for the top of atmosphere net energy flux

"conservation" does a new check we made plotting mass, axial angular momentum and kinetic energy as the run progresses. It should just run and get the most up to date data (make sure the paths are correct as this script was made using um-serve not process.astro). The graph of interest is the one which compares the three plots for the 1x and 10x metallicity runs. Below this in the same script are some plots of contoured wind vectors at different pressure levels

rotating_winds does some funky processing on the wind vectors, you should be able to run the script and again it grabs the most up to date files, itll take a bit of time to run but at the end it outputs a fancy gif. 

The rest are the various scripts i've got making different transmission spectra. 

(good luck)




