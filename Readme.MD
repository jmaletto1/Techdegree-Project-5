Unit-5 Techdegree Project

This system allows users (who do not need to register/login) the ability to post, view, edit and delete journal updates.

App.py runs the app, connects and closes the database connection using before_request() and after_request(). It sets the following routes/methods:

index() - Displays the stream of journal entries.

create() - Adds a new entry to the journal.

show(id) - Allows the user to view the full page of specific journal.

edit(id) - Allows the user to edit the info of a given journal entry.

delete (id) - Allows the user to remove a journal enty.

At the bottom of the file, the app initialises the model if __name__ == '__main__':

----

Models.py creates the Journal Class (Model), and the classmethod that adds an entry.

Forms.py creates the class that processes the data provided by the user.

The info is then processed onto the pages 'index.html', 'edit.html', 'detail.html' and 'new.html' using the pre-supplied css.