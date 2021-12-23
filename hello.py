import dearpygui.dearpygui as dpg

rem = 12

def on_main_window_close():
    exit(0)

def save_callback():
    print("Save Clicked")

def main():
    tasks = []
    def add_task():
        nonlocal tasks
        pass


    dpg.create_context()

    with dpg.window(label="Main Window", autosize=True, on_close=on_main_window_close):
        with dpg.collapsing_header(label="Add Task", leaf=True):
            with dpg.group(indent=rem):
                with dpg.group(horizontal=True):
                    dpg.add_input_text(hint="URL")
                    dpg.add_button(label="Add Task", callback=add_task)
                dpg.add_checkbox(label="Add on Clipboard Change")
        with dpg.collapsing_header(label="Staging", leaf=True):
            with dpg.group(indent=rem):
                dpg.add_text("Pending Tasks")
                listbox_tasks = dpg.add_listbox()
        with dpg.collapsing_header(label="Downloading", leaf=True):
            with dpg.group(indent=rem):
                dpg.add_text("TODO")

    dpg.create_viewport()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
