Bad Radio

I was recording a radio station the other day and suddenly the frequency gets hijacked with some kind of weird signal?? This is the audio file, hopefully you can extract something out of it.

Steps:
- audio file contains morse code that informs the listener to download the Android app Robot36 to decode SSTV signal
- SSTV contains link to https://rentry.org/bad-radio, contains a photo with a message hidden with LSB (exif description is a rick roll kinda)
- The hidden message is a QR code to a flag, the flag in question is a webm file compressed with zstandard
- decompress zst file with zstd command, output decompressed webm
- webm contains 8 seemingly flickering blocks on an interval but they actually encode characters sequentially
- when decoded, it will produce a string with 4 base64 encoded messages, one of them is the actual flag

Flag: slashroot7{R4di0_h4s_B33n_T0uhoU_h1JAck3D_w_4pPPl3_Z0MG}

Notes:
- only upload 09-06-2023_20.28.30.wav, AND NOTHING ELSE
- rentry password: WgrVbUKIqYw7e69NCV0gZfeVTJdkBINv