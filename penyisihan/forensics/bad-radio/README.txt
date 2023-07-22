Bad Radio

I was recording a radio station the other day and suddenly the frequency gets hijacked with some kind of weird signal?? This is the audio file, hopefully you can extract something out of it.

Steps:
- audio file contains morse code that informs the listener to download the Android app Robot36 to decode SSTV signal
- SSTV contains link to https://rentry.org/bad-radio, informs the viewer to download a file called flag.mp4.zst.enc, and key
- xor the enc with the key to get unencrypted zst
- decompress zst file with zstd command, output decompressed mp4
- mp4 contains flag scattered throughout the video

Flag: slashroot7{R4di0_h4s_B33n_T0uhoU_h1JAck3D_w_4pPPl3_Z0MG}

Notes:
- only upload 09-06-2023_20.28.30.wav, AND NOTHING ELSE
- rentry password: WgrVbUKIqYw7e69NCV0gZfeVTJdkBINv