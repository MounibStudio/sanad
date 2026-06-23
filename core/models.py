import uuid
from django.db import models


class Session(models.Model):
    """Represents one usage session (browser tab / anonymous visit)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)


class HistoryEntry(models.Model):
    """One Q&A pair saved locally for the offline history feature (F12)."""
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='history',
        null=True,
        blank=True,
    )
    question_text = models.TextField()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'History Entry'
        verbose_name_plural = 'History Entries'

    def __str__(self):
        return self.question_text[:60]
