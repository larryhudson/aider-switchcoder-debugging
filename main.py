from aider.coders import Coder
from aider.models import Model
from aider.io import InputOutput

def main():
    model = Model("claude-3-5-sonnet-20240620")
    io = InputOutput(yes=True)
    fnames = ['README.md']
    coder = Coder.create(main_model=model, fnames=fnames, io=io, stream=False, suggest_shell_commands=False)

    prompt = "Please add a hello world message to the README file."
    changes_result = coder.run(prompt)

    summary_coder = Coder.create(main_model=model, fnames=fnames, io=io, stream=False, suggest_shell_commands=False, from_coder=coder)
    summary_result = summary_coder.run("/ask Thank you. Please write a description of the changes you have made. This will be included in the pull request description.")

    print("Changes result:")
    print(changes_result)

    print("Summary result:")
    print(summary_result)

if __name__ == "__main__":
    main()
