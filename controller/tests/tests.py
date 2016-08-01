from django.test import TestCase


class ViewTests(TestCase):

    def test_home_view_renders_home_template(self):
        response = self.client.get("/home")
        self.assertTemplateUsed("home.html")

    def test_about_view_renders_about_template(self):
        response = self.client.get("/about")
        self.assertTemplateUsed("about.html")
