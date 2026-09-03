# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Notes

"""
These tests is created to test the functionality of the Notes model class as
well as the views created to test the create, read, update and delete functions
of the sticky notes app. I researched some test methods such as to test re-
directs and some other methods in Django's testing documentation.
https://docs.djangoproject.com/en/6.1/topics/testing/tools/
"""


class NotesModelTest(TestCase):
    def setUp(self):
        """
        In the setup method, the note object for the purpose of testing is
        created.
        """
        Notes.objects.create(title='Test Note', content='Testing content')


    def test_note_title(self):
        """
        This is the test to confirm if the title object has the expected title.
        """
        note = Notes.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')


    def test_note_content(self):
        """
        This test will confirm if the note content object has the correct
        content.
        """
        note = Notes.objects.get(id=1)
        self.assertEqual(note.content, 'Testing content')


class NotesViewTest(TestCase):
    def setUp(self):
        """
        The setup method creates the notes for use in the testing.
        """
        self.note1 = Notes.objects.create(title='Test note 1',
                                          content='First test note')
        self.note2 = Notes.objects.create(title='Test note 2',
                                          content='Another test note!')


    def test_notes_view(self):
        """
        This is the test for the notes_view view. It will test correct status,
        confirm if the notes display in the view and confirms if the corret
        template is used.
        """
        response = self.client.get(reverse('notes_view'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test note 1')
        self.assertContains(response, 'Test note 2')
        self.assertTemplateUsed(response, 'notes/notes_view.html')
        

    def test_notes_detail(self):
        """
        This is the test for the notes_detail view. It tests the correct
        status, confirms if the correct note requested is displaying and
        confirms if the correct template is used.
        """
        response = self.client.get(reverse('notes_detail',
                                           args=[self.note2.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_detail.html')
        self.assertContains(response, 'Test note 2')
        self.assertContains(response, 'Another test note!')


    def test_notes_create_get(self):
        """
        This test is testing if the form renders successfully from a GET
        request in the notes_create view and if the correct template is used.
        """
        response = self.client.get(reverse('notes_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_form.html')
        self.assertIn('form', response.context)


    def test_notes_create_post(self):
        """
        This test is testing if a note is successfully created from a POST
        request in the notes_create_view, confirms if the page redirects to
        
        """
        data_form = {
            'title': 'New Note',
            'content': 'This is a new note'
        }

        response = self.client.post(reverse('notes_create'), data=data_form)

        self.assertRedirects(response, reverse('notes_view'))
        self.assertTrue(Notes.objects.filter(title='New Note').exists())


    def test_notes_update(self):
        """
        This test is testing if the notes are updating correctly in the
        notes_update view.
        """
        data_form = {
            'title':'Updated!',
            'content':'Note successfully updated'
        }

        response = self.client.post(reverse('notes_update',
                                            args=[self.note1.pk]),
                                    data=data_form)

        self.assertRedirects(response, reverse('notes_view'))
        self.note1.refresh_from_db()
        self.assertEqual(self.note1.title, 'Updated!')
        self.assertEqual(self.note1.content, 'Note successfully updated')


    def test_notes_delete(self):
        """
        This test is testing of the notes are successfully deleted in the
        notes_delete view.
        """
        response = self.client.post(reverse('notes_delete',
                                            args=[self.note1.pk]))

        self.assertFalse(Notes.objects.filter(pk=self.note1.pk).exists())
        
        
