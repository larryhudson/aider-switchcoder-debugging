# Debugging an issue with Aider

I'm running into this error when trying to use a `/ask` command in Aider when scripting:

```
Traceback (most recent call last):
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/main.py", line 24, in <module>
    main()
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/main.py", line 15, in main
    summary_result = summary_coder.run("/ask Thank you. Please write a description of the changes you have made. This will be included in the pull request description.")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/coders/base_coder.py", line 717, in run
    self.run_one(with_message, preproc)
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/coders/base_coder.py", line 760, in run_one
    message = self.preproc_user_input(user_message)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/coders/base_coder.py", line 749, in preproc_user_input
    return self.commands.run(inp)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/commands.py", line 221, in run
    return self.do_run(matching_commands[0][1:], rest_inp)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/commands.py", line 196, in do_run
    return cmd_method(args)
           ^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/commands.py", line 942, in cmd_ask
    return self._generic_chat_command(args, "ask")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/larryhudson/github.com/larryhudson/aider-switchcoder-debugging/venv/lib/python3.12/site-packages/aider/commands.py", line 965, in _generic_chat_command
    raise SwitchCoder(
aider.commands.SwitchCoder
```

To reproduce:
- Clone this repo
- Create a new virtual environment - python -m venv venv
- Install dependencies - pip install -r requirements.txt
- Make sure ANTHROPIC_API_KEY is set in your environment
- Run python main.py to run the script
