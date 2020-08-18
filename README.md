This is a python request based module for supreme in store sign ups for this season.
You still need to do 2 things:

1, have a captcha harvester. There are many open source ones lying around. Supreme uses v2 captcha.
you will have to change line 18 to your own captcha harvester's get ip, or the fucntion to
however you intend to retrieve captcha tokens


2, fill in your custom info. lines 150-170. this is just your billing info and what not.
it is commented too so it should be self explanatory.

for locations, currently there is 'Manhattan', 'Brooklyn', 'Los Angeles', and 'San Francisco'
