# Simple_Powershell_Obfuscator

*tool for powershell script obfuscation*

# example

#### Reverse shell script written in C#. 
> The script is provided for educational purposes only and should not be used for malicious activities.

![Alt Text](image2.PNG)

*After compiling the C# program, a simple PowerShell script is provided to load the assembly and invoke the main method of the executable.*

![Alt Text](image4.PNG)

*After executing the tool, we received an obfuscated version of the initial script, now named `obfuscated.ps1`*

![Alt Text](image5.PNG)

*We then start a listener on the attacker's machine and execute the `obfuscated.ps1` script on the victim's machine*

![Alt Text](image3.PNG)
![Alt Text](image1.PNG)

> And we got the shell!
