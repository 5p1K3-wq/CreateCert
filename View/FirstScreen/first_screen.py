%s
from View.base_screen import BaseScreenView


class %s(BaseScreenView):
    """Implements the login start screen in the user application."""
%s
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        %s