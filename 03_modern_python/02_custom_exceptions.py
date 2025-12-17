class AppBaseError(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(AppBaseError):
    """Raised when data validation fails."""
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field

def validate_user(username: str):
    if len(username) < 3:
        raise ValidationError("Username too short", field="username")

try:
    validate_user("jo")
except ValidationError as e:
    print(f"Error in {e.field}: {e}")
else:
    # Runs ONLY if no exception was raised
    print("Validation successful!")
finally:
    # Always runs (cleanup logic)
    print("Execution finished.")