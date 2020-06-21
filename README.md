# VideoDownloader
A simple video downloader that I created for my sister
# VideoDownloader
This is a simple video downloader that I made for my sister.

As her school was closed due to COVID-19, she had online classes from a third party training institution. They uploaded tutorial videos to their website with no download option. They also put a deadline after which they remove the uploaded videos.

My sister was unable to view some videos uploaded on June 2020 and the deadline was close by. So, I decided to help her in downloading the videos.

Initially, I tried to get a link to the video by inspecting it. But I found that they were dynamically fetching parts of the video as **``.ts``** files. Each of these files contain only a small portion of the video ( aprox. 10 seconds ). But the interesting thing about them is that they are public ( does not require any authentication token for downloading a part if you know the url ), and each part was named in a sequential order ( like 00001.ts, 00002.ts etc... ).

## How to use this tool
I am having a Linux system, and so, I am using utilities found in Linux. The overall working is as follows:

 1. Generate a text file containing the URL of all ts files ( parts of video )
 2. Download all these parts using a program called **wget**. The text file generated in step 1 will be used as input for the wget command.
 3. Combine all the downloaded ts files into a single ts file
 4. Convert the ts file generated in step 3 into a mp4 video file

##### Step 1: Generate text file
I have written a simple Java program - Generate.java which can be used to generate the text file containing all URLs. Edit this program according to your URL. Then compile it with command `` java Generate.java `` and run it with command `` java Generate ``. The program will generate a text file `` urls.txt ``.
##### Step 2: Download the files
From your Linux terminal, run the `` download.sh `` shell script. Make sure that the download script is run from the same directory that contains the `` urls.txt `` file. The script will produce a beep sound after the download completes.
##### Step 3: Combine the files to produce the output file
From your linux terminal, run the `` concat.sh `` shell script. Make sure that the concat script is run from the same directory that contains all the downloaded `` .ts `` files. The script will generate an output file named `` all.mp4 `` which is the full length video generated from the individual `` .ts `` files.

> **Note:** You won't be knowing exactly how many parts are there for a video. So, generate a `` urls.txt `` file that has a greater number of URLs. The downloader will automatically handle that.

> **Note:** You will need JDK for compiling the Java program. Feel free to use any other method to the generate the ``urls.txt`` file. The only thing to remember is that you need to have one URL per line.

> **Note:** To get the initial URL, inspect your browser's network tab while you are on the webpage containing the video, and look for a request fetching file with ``.ts`` extension.

> **Note:** You need the following programs on your Linux system for running the scripts:
> ``wget`` - for downloading the files
> ``ffmpeg`` - for converting the ts file to mp4
> ``speaker-test`` - for getting the beep sound after the download completes
