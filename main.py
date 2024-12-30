from taipy.gui import Gui
import taipy.gui.builder as tgb

# Define the root page with navigation
with tgb.Page() as root_page:
    tgb.navbar()  # Default navigation bar
    tgb.text("# Welcome to the Multi-Page Application", mode="md")

# Define Page 1
with tgb.Page() as page_1:
    tgb.text("## This is Page 1", mode="md")

# Define Page 2
with tgb.Page() as page_2:
    tgb.text("## This is Page 2", mode="md")

# Combine all pages
pages = {
    "/": root_page,
    "page1": page_1,
    "page2": page_2
}

# Run the application
Gui(pages=pages).run()





### The code below shows Layouts in Taipy II
    #Dialogs allow you to present content in a modal window over the main application page. Users can interact with the dialog, which can be closed via buttons or by clicking outside the dialog area. and the answer after choosing a button, is shown in the terminal 😋.
# import taipy.gui.builder as tgb
# from taipy.gui import Gui

# show_dialog = False

# def dialog_action(state, _, payload):
#     if payload["args"][0] == 0:
#         print("Good to hear!")
#     elif payload["args"][0] == 1:
#         print("Sorry to hear that.")
#     else:
#         print("Ok bye.")
#     state.show_dialog = False

# with tgb.Page() as page:
#     with tgb.dialog("{show_dialog}", title="Welcome!", on_action=dialog_action, labels="Couldn't be better;Not my day"):
#         tgb.html("h2", "Hello!")

#     tgb.button("Show", on_action=lambda s: s.assign("show_dialog", True))

# if __name__ == "__main__":
#     Gui(page).run(title="Dialog - Labels")
