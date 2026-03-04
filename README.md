# Sentinel One Passphrase Exporter

Created for Offboarding Engineers in order to backup any offline active or "decommed" device passphrases prior to site deletion.

> The passphrases can then be used to uninstall an orphaned Sentinel One install 

---

## Features

- Option to change output folder (User's documents folder is default)
- Simple, single page GUI

---

## Requirements

### If running main.py directly:
- Python 3.14 
- pip install requests

### If running the packaged .exe:
- OS: Windows 10 or later
- No install required
- The packaged exe only offers options for company specific URLs, in order to use this with other URLs, see instructions under Installation

### Sentinel One Portal Requirements

- Site ID of the site being exported
- API key of an admin service user of the site being exported 
---

## Installation

### Option 1: Clone the repository

```bash
git clone https://github.com/JoshSmith84/s1_passhprases.git
cd s1_passphrases
```

- Edit constants.py with your own URLs. You can also set an API constant if you wish to use a root level service user with admin rights to all sites.... If the API constant is not set, the program will prompt instead