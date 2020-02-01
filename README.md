# fb-export-to-slack
Import Facebook Messenger Group chats or single user chats into Slack. This converts a Facebook Messenger JSON file export to a Slack CSV file, which can then be imported into Slack.

## How to use

### Downloading your Facebook data

- go to https://www.facebook.com/settings?tab=your_facebook_information
- click on "Download my information"
- click "Deselect All"
- click on Messages
- for the data export format, change HTML to JSON
- set the media quality to low (this cannot import images)
- click Create File
- follow the instructions, then download the ZIP file
- there will be a lot of folders. Search for the group or person's name to find the folder that contains the JSON file.
- select the file called `message.json` and open it up to confirm that it has your messages that you'd like to import
- run the following command: `python3 fb_to_slack.py /path/to/message.json /path/to/output.csv`
- the resulting CSV file can be imported into Slack. For the delimiter on Slack's import page, choose `,` (default)
- press import, and within a few minutes, all of your messages from your Facebook group or user will appear in the designated Slack channel

## Bugs

- stickers and images are not imported
- not tested with anything other than English text
