from __future__ import print_function

import argparse
import os
import sys
import oss2
import time
import operator
from itertools import islice

FLAGS = None

# ------------------ SET YOUR OWN INFORMATION HERE !! ------------------------ #
# Those infomation is used frequently。 Put it at the top of scripts
#                    AccessKeyId              AccessKeySecret
auth = oss2.Auth("LTAIeitJrN8PGR66", "lp4lDWOuFBVhsLffUquOsk8TN5L549")

# Internal endpoint (See it at your oss control panel)
endpoint = 'http://oss-cn-beijing.aliyuncs.com'

# Public endpoint
public_endpoint = 'http://oss-cn-beijing.aliyuncs.com'

# Your bucket name
bucket_name = "feifeidata"



def uploadFiles(bucket):
    """ uploadFiles
    Upload FLAGS.files to the oss
    """

    start_time = time.time()

    for tmp_file in FLAGS.files:
        if not os.path.exists(tmp_file):
            print("File {0} is not exists!".format(tmp_file))
        else:
            print("Will upload {0} to the oss!".format(tmp_file))

            tmp_time = time.time()
            # cut the file name
            filename = tmp_file[tmp_file.rfind("/") + 1: len(tmp_file)]
            ossFilename = os.path.join(FLAGS.prefix, filename)
            oss2.resumable_upload(
                bucket,
                ossFilename,
                tmp_file,
                progress_callback=percentage)

            print("\nFile {0} -> {1} uploads finished, cost {2} Sec.".format(
                tmp_file, ossFilename, time.time() - tmp_time))

    print("All upload tasks have finished!")
    print("Cost {0} Sec.".format(time.time() - start_time))



def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')

        sys.stdout.flush()


def main():
    """ main function
    """
    # creat the bucket
    # auth = oss2.Auth("LTAIBmrcaxHaSMuP", "byOt6OmeHE4aRUjwBDtSbcESLsxkxH")

    # download from aliyun interal domain
    # endpoint = "http://oss-cn-beijing-internal.aliyuncs.com"
    # download from public domain
    # cname = "http://oss.mcoder.cc"

    if FLAGS.internal:
        # if using internal ECS network
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        tmp_endpoint = endpoint
    else:
        bucket = oss2.Bucket(auth, public_endpoint, bucket_name)
        tmp_endpoint = public_endpoint

    print("Your oss endpoint is {0}, the bucket is {1}".format(
        tmp_endpoint, bucket_name))


    uploadFiles(bucket)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        dest='files',
        action='append',
        default=[],
        help='the file name you want to download!')

    parser.add_argument(
        "-l",
        "--listfiles",
        default=False,
        dest="listFiles",
        action="store_true",
        help="If been True, list the All the files on the oss !")

    parser.add_argument(
        "-o",
        "--outputPath",
        dest="outputPath",
        default="./",
        type=str,
        help="the floder we want to save the files!")

    parser.add_argument(
        "-i",
        "--internal",
        dest="internal",
        default=False,
        action="store_true",
        help="if you using the internal network of aliyun ECS !")

    parser.add_argument(
        "--upload",
        dest="upload",
        default=False,
        action="store_true",
        help="If been used, the mode will be select local files to upload!")

    parser.add_argument(
        "-p",
        "--prefix",
        dest="prefix",
        default="",
        type=str,
        help="the prefix add to the upload files!")

    FLAGS, unparsed = parser.parse_known_args()

    print(FLAGS)  # print the arguments
    main()
