try:
    import oss2
except:
    oss2 = None


def get_bucket(bucket_name='feifeidata'):
    auth = oss2.Auth('LTAIeitJrN8PGR66', 'lp4lDWOuFBVhsLffUquOsk8TN5L549 ')
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', bucket_name)
    return bucket


if __name__ == '__main__':
    bucket = get_bucket()
    bucket.put_object('report/201903/out4.png', 'D:\mytoos\\uwsgi_\\out4.png')
