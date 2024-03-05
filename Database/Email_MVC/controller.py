import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EmailAddress


class Controller:
    def __init__(self, engine_address='sqlite:///emails.sqlite'):
        self.engine = create_engine(engine_address, echo=True)

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            # save the model
            with Session(self.engine) as sess:
                email_address = EmailAddress(email=email)
                sess.add(email_address)
                sess.commit()

            # show a success message
            return f'The email {email} saved!'

        except ValueError as error:
            # Validation has failed - reraise the error for the view
            raise ValueError(error)

        except sqlalchemy.exc.IntegrityError:
            error_message = f'{email} is already in the database'
            raise ValueError(error_message)


if __name__ == "__main__":
    my_controller = Controller()
    my_controller.save('agdales101@highgate.co.uk')