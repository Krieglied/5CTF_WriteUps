For this challenge, first an encrypted powerpoint, based on the novel A Tale of Two Cities, was provided to be cracked.  Loading in a text copy of the novel as the wordlist for hashcat, the encrypted zip file was cracked.  The next challenge provided the non-encrypted version of the powerpoint.
For the rest of the challenges, the non-encrypted powerpoint was loaded with various flags.  Below, I'm just going to list the methods that I used to find various flags in the powerpoint file.

- looking at the /docProps/core.xml file, under the creator tag
- on pages 5,10,15,20 and 25, there are comments from the referenced user, that are 4 hex strings of two characters each.  Put through a hex-to-ascii to get the message
- search through the slides.xml files
- search through the slideLayouts.xml template file
- search through the notes.xml files
- gotten through subtitle on front page, also looking through the slides.xml files
- on page 2, the english section has small text in the whitespace. found easily by copying text into english to french translate
- on page 45, image has encoded flag in description of alt text.  flag is an anagram of that text
- found by converting pptx to zip, unzipping it, running exiftool on image65.png (rusty blade picture), looking at Description field
- steghide on found secret.jpg, no passphrase
