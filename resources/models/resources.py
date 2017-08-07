from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

from modelcluster.contrib.taggit import ClusterTaggableManager
from django.db.models.fields import TextField, URLField, IntegerField

from resources.models.tags import TopicTag, IssueTag, ReasonTag, ContentTag, HiddenTag


class ResourceIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super(ResourceIndexPage, self).get_context(request)
        resources = self.get_children().live().order_by('-first_published_at')
        context['resources'] = resources
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ResourcePage(Page):
    heading = TextField(blank=True, help_text="The title of the resource being linked to")
    resource_url = URLField(blank=True, help_text="The url of the resource to link to")
    body = RichTextField(blank=True, help_text="A description of the resource")
    pros = RichTextField(blank=True, help_text="A list of pros for the resource")
    cons = RichTextField(blank=True, help_text="A list of cons for the resource")
    video_url = URLField(blank=True, help_text="URL of a youtube video for the resource")

    topic_tags = ClusterTaggableManager(
        through=TopicTag, blank=True,
        verbose_name='Topic Tags', related_name='resource_topic_tags',
        help_text='Topic tags, eg: "sleep", "depression", "stress"'
    )
    issue_tags = ClusterTaggableManager(
        through=IssueTag, blank=True,
        verbose_name='Issue Tags', related_name='resource_issue_tags',
        help_text='Issue tags, eg: "insomnia", "fatigue", "snoring"'
    )
    reason_tags = ClusterTaggableManager(
        through=ReasonTag, blank=True,
        verbose_name='Reason Tags', related_name='resource_reason_tags',
        help_text='Reason tags, eg: "loneliness", "relationships"'
    )
    content_tags = ClusterTaggableManager(
        through=ContentTag, blank=True,
        verbose_name='Content Tags', related_name='resource_content_tags',
        help_text='Content Type tags, eg: "videos", "blogs", "free", "subscription"'
    )
    hidden_tags = ClusterTaggableManager(
        through=HiddenTag, blank=True,
        verbose_name='Hidden Tags', related_name='resource_hidden_tags',
        help_text='Hidden tags for admin use'
    )
    PRIORITY_CHOICES = (
      (1, '1'),
      (2, '2'),
      (3, '3'),
      (4, '4'),
      (5, '5'),
    )
    priority = IntegerField(
      choices=PRIORITY_CHOICES,
      default='5',
      help_text='Highest priority 1, lowest priority 5'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('pros'),
        index.SearchField('cons'),
        index.SearchField('heading'),
        index.SearchField('resource_url'),
        index.RelatedFields('issue_tags', [
            index.SearchField('name'),
        ]),
        index.RelatedFields('content_tags', [
            index.SearchField('name'),
        ]),
        index.RelatedFields('reason_tags', [
            index.SearchField('name'),
        ]),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading', classname="full"),
        FieldPanel('resource_url', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('pros', classname="full"),
        FieldPanel('cons', classname="full"),
        FieldPanel('video_url', classname="full"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('topic_tags'),
        FieldPanel('issue_tags'),
        FieldPanel('reason_tags'),
        FieldPanel('content_tags'),
        FieldPanel('hidden_tags'),
        FieldPanel('priority'),
    ]

    class Meta:
        verbose_name = "Resource"
