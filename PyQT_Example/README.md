# Automator (Batch Script UI)
This is an example of a UI for a batch processing application I created. It dynamically populates all the production 
(episode, shot, asset, task, etc.) from Shotgun (through a Flask proxy server to resolve requests). 

This lets artist load batch scripts that can then be sent as jobs to the farms. This flexible design allows artists 
to iterate over many different types of entities with many different tasks from a single UI.