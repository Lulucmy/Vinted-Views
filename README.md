# Vinted-Views

🤖 A simple bot that increases the amount of views of all the articles you're selling on Vinted

💸 Boost your sales and items without paying 

![vinted_views_bot](https://i.imgur.com/ZqhabGT.png)

## Features


- Easy configuration / One library needed
- Fetch all articles of a Vinted profile
- Add views to your items undefinitely

## Installation

This script only needs the [`requests`](https://pypi.org/project/requests/) package. Install it with:
- `pip install requests`

Then, add the username of the account you want to boost in the config.py file:

```py
config = {
    'username' : "YourUsername",     #Your username on Vinted
    'country'  : "FR",               #Your profile's main country (eg: FR for France/ES for Spain)
    'cooldown' : "true"              #True adds a cooldown between views
}
```

Finally, run `python3 main.py` and let the magic begin ✨ 
