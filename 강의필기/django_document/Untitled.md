#MTM(self)

Relation.objects.create(from_user=user2,to_user=user3)
```
user1.follow_relations.all()
```

쿼리셋으로 Relation from user1 to user2

```
user2.follower_relations.all()
```
쿼리셋으로 Relation form user user2


```
Relation.objects.get_or_create(from_user=user1 , to_user=user2)
```

```
user1.follower_relations.filter()
```

```
Relation.objects.filter(to_user=user1).filter()
```
