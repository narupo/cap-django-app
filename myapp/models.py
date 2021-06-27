{@
	ms = opts.get("m") or opts.get("models")
	names = []
	if ms:
		names = ms.split(",")
	end
@}from django.db import models


{@
	for i = 0; i < len(names); i += 1:
		n = names[i]
		N = names[i]
@}class {: N :}(models.Model):
    TODO = models.CharField(max_length=255, help_text='TODO')
    created = models.DateTimeField(auto_now_add=True, help_text='作成日')
    modified = models.DateTimeField(auto_now=True, help_text='更新日')

    class Meta:
        verbose_name = '{: N :}'
        verbose_name_plural = '{: N :}一覧'
        ordering = ('-id', )

    def __str__(self):
        return f'({self.id}) {self.TODO}'


{@
	end
@}

