from django.test import TestCase


class ViewTests(TestCase):

    def test_home_view_renders_home_template(self):
        response = self.client.get("/home")
        self.assertTemplateUsed("home.html")

    def test_about_view_renders_about_template(self):
        response = self.client.get("/about")
        self.assertTemplateUsed("about.html")

    def test_blog_view_renders_blog_template(self):
        response = self.client.get("/blog")
        self.assertTemplateUsed("blog.html")

    def test_projects_view_renders_projects_template(self):
        response = self.client.get("/projects")
        self.assertTemplateUsed("projects.html")

    def test_other_view_renders_other_template(self):
        response = self.client.get("/other")
        self.assertTemplateUsed("other.html")
