class Blog(object):
    def read(self):
        print('Read the blog')
    
    def write(self):
        print('Write the blog')

# Keep sub-class proxy independent of real subject
class Proxy(object):
    def __init__(self, target):
        self.target = target
    
    def __getattr__(self, attr):
        return getattr(self.target, attr)

# However, you have to write higher-level proxy and overwrite the interface
class AnonUserBlogProxy(Proxy):
    def __init__(self, blog):
        super().__init__(blog)
    
    # overwrite write method
    def write(self):
        print('Only authorized user can write blog posts.')

if __name__ == '__main__':
    blog = Blog()
    blog.write()
    print('='*50)
    proxy = AnonUserBlogProxy(blog)
    proxy.write()