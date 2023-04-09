import webbrowser
from datetime import datetime

import AppKit
import rumps


def quit_app(_):
    """Quit the application."""
    rumps.quit_application()


def days_remaining():
    """Calculate the number of days remaining until a target date."""
    target_date = datetime(2023, 5, 20, 2, 40, 50)
    today = datetime.now()
    remaining_days = (target_date - today).days
    return remaining_days


def create_text_field_with_properties(text, x, y, width, height, alignment, text_color=None):
    """Create a text field with the given properties."""
    text_field = AppKit.NSTextField.alloc().initWithFrame_(
        AppKit.NSMakeRect(x, y, width, height)
    )
    text_field.setStringValue_(text)
    text_field.setBezeled_(False)
    text_field.setDrawsBackground_(False)
    text_field.setEditable_(False)
    text_field.setSelectable_(False)
    text_field.setLineBreakMode_(AppKit.NSLineBreakByWordWrapping)
    text_field.setAlignment_(alignment)
    if text_color:
        text_field.setTextColor_(text_color)
    return text_field


def show_welcome_message(_):
    """Show a welcome message."""
    message = (
        "this is your captain farza speakin. sup?\n\n"
        "welcome to s3. you're here. don't underestimate how far you can get in just six weeks.\n\n"
        "xo,\n"
        "farza\n\n"
        "ps. isn't this fkin cool?\n\n"
    )

    left_text = "from farza's desk / 001"
    right_text = "sat april 8 23"

    alert = AppKit.NSAlert.alloc().init()
    alert.setMessageText_("welcome")

    main_text_field = create_text_field_with_properties(
        message, 0, 20, 400, 150, AppKit.NSLeftTextAlignment
    )
    gray_color = AppKit.NSColor.grayColor()
    left_text_field = create_text_field_with_properties(
        left_text, 0, 0, 200, 20, AppKit.NSLeftTextAlignment, gray_color
    )
    right_text_field = create_text_field_with_properties(
        right_text, 200, 0, 200, 20, AppKit.NSRightTextAlignment, gray_color
    )
    container_view = AppKit.NSView.alloc().initWithFrame_(
    AppKit.NSMakeRect(0, 0, 400, 170)
)
    container_view.addSubview_(main_text_field)
    container_view.addSubview_(left_text_field)
    container_view.addSubview_(right_text_field)

    alert.setAccessoryView_(container_view)
    alert.setIcon_(AppKit.NSImage.alloc().initWithContentsOfFile_("logo.png"))
    alert.runModal()

class MenuBarApp(rumps.App):
    """A menu bar app."""
    def __init__(self):
        """Initialize the app."""
        super(MenuBarApp, self).__init__("Days Remaining", icon="icon.icns")
        self.menu = self.create_menu()
        self.title = self.get_title()

    def create_menu(self):
        """Create the menu for the app."""
        menu = [
            rumps.MenuItem("welcome", callback=show_welcome_message),
            self.create_assets_menu(),
            rumps.MenuItem("quit", callback=quit_app),
        ]
        return menu

    def create_assets_menu(self):
        """Create the assets menu."""
        assets_menu = rumps.MenuItem("assets")
        assets_menu.add(
            rumps.MenuItem(
                "spectreseek",
                callback=lambda _: webbrowser.open(
                    "https://framerusercontent.com/images/A4ATGSFzLdUkscJGEJAl1xoRg.png"
                ),
            )
        )
        assets_menu.add(
            rumps.MenuItem(
                "alterok",
                callback=lambda _: webbrowser.open(
                    "https://framerusercontent.com/images/amo7e1yQz0pEcRbaZFObkTpQIjc.png"
                ),
            )
        )
        assets_menu.add(
            rumps.MenuItem(
                "gaudmire",
                callback=lambda _: webbrowser.open(
                    "https://framerusercontent.com/images/3HszPak0gJ3FySgT9VG9uk02j4.png"
                ),
            )
        )
        assets_menu.add(
            rumps.MenuItem(
                "erevald",
                callback=lambda _: webbrowser.open(
                    "https://framerusercontent.com/images/kzNIFbdmcPta67CoMrd1x93h9o0.png"
                ),
            )
        )
        return assets_menu

    def get_title(self):
        """Get the title for the app."""
        return f" {days_remaining()} days left"

    @rumps.timer(60)  # update every minute
    def update_title(self, sender):
        """Update the title of the app."""
        self.title = self.get_title()

app = MenuBarApp()
app.quit_button = None
app.run()
