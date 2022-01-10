import time
import os

from checks import AgentCheck

class FileCheck(AgentCheck):
    def check(self, instance):

        if 'filepath' not in instance:
            self.log.info("Skipping instance, no filepath defined.")
            return

        filepath = instance['filepath']
        result = AgentCheck.CRITICAL
        message = "File "+i filepath+" does not exists, or is unreachable";

        filecheck_tags = self.instance.get('tags', [])
        filecheck_tags.append('path:{}'.format(path))

        if os.path.isfile(filepath):
            result = AgentCheck.OK
            message = "File "+ filepath +" exists"

            st=os.stat(filepath)
            mtime=st.st_mtime
            age=time.time()-mtime
            self.gauge('filecheck.modified',mtime,tags=filecheck_tags)
            self.gauge('filecheck.age',age,tags=filecheck_tags)

        self.service_check('filecheck.exists',result,tags=filecheck_tags,message=message)

if __name__ == '__main__':
    print ("...")