```
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase

User = get_user_model()


class UserModelTest(TransactionTestCase):
    DUMMY_USERNAME = "username"
    DUMMY_PASSWORD = 'password'

    @staticmethod
    def make_users(num):
        return [User.objects.create_user(username='username{}'.format(i)) for i in range(num)]

    def test_fields_default_value(self):
        user = User.objects.create_user(
            username=self.DUMMY_USERNAME,
            password=self.DUMMY_PASSWORD,
        )
        # first_name
        self.assertEqual(user.first_name, '')
        # last_name
        self.assertEqual(user.last_name, '')
        # 유저타입
        self.assertEqual(user.user_type, User.USER_TYPE_DJANGO)
        # 닉네임
        self.assertEqual(user.nickname, None)
        # 이미지
        self.assertEqual(user.img_profile, '')
        # relations
        self.assertEqual(user.relations.count(), 0)

    def test_follow(self):
        def follow_test_helper(source, following, non_following=None):
            for target in following:
                self.assertIn(target, source.following)
                self.assertIn(source, target.following)
                self.assertTrue(source.is_follow(target))
                self.assertTrue(target.is_follower(source))
            for target in non_following:
                self.assertNotIn(target, source.following)
                self.assertNotIn(source, target.followers)
                self.assertFalse(source.is_follow(target))
                self.assertFalse(target.is_follower(source))

        user1, user2, user3, user4 = self.make_users(4)

        user1.follow(user2)
        user1.follow(user3)
        user1.follow(user4)

        user2.follow(user3)
        user2.follow(user4)

        user3.follow(user4)

        follow_test_helper(source=user1,
                           following=[user2, user3, user4],
                           non_following=[]
                           )

        follow_test_helper(source=user2,
                           following=[user3, user4],
                           non_following=[user1]
                           )
        follow_test_helper(source=user3,
                           following=[user4],
                           non_following=[user1, user2]
                           )
        follow_test_helper(source=user4,
                           following=[],
                           non_following=[user1, user2, user3]
                           )

    def test_unfollow(self):
        user1, user2 = self.make_users(2)
        user1.follow(user2)

        self.assertTrue(user1.is_follow(user2))
        self.assertTrue(user2.is_follower(user1))
        self.assertIn(user1, user2.followers)
        self.assertIn(user2, user1.follwing)

        user1.unfollow(user2)
        self.assertFalse(user1.is_follow(user2))
        self.assertFalse(user2.is_follower(user1))
        self.assertNotIn(user1, user2.followers)
        self.assertNotIn(user2, user1.follwing)

```