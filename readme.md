I wanted to dump my contacts from Google into texted.io.  Texted allows you to upload 100 contacts (first/last/number) at a time.  So I made a way to programmatically pull that info and create 100-contact files.

First, in contacts.google.com, go to old view, then export CSV <b>for Outlook</b> (if you do it for Google, weird characters will be used).  That file should be called `contacts.csv` by default.  Then just run the python script and it'll generate the appropriate number of csvs to upload.

When uploading on texted.io, I ran into an error where after every upload it spit back an error alert saying some bug had been detected.  When I refresh the browser, the contacts are all there though, so.../shrug

This only currently works if the contact's number is stored as "Mobile" in Google contacts
