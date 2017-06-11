# ipython

%load_ext autoreload

%autoreload 2


# related

```
 recommender = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='tradeinfo_set_by_recommender'

    )
```

```
class Club(models.Model):
    name = models.CharField(max_length=60)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
        through_fields=('club', 'player'),
    )
```