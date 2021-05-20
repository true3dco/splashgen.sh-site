from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="Splashgen - Landing Pages Built In Python",
                  theme="dark")
site.headline = "Build your landing page in python effortlessly"
site.subtext = """
In less than 20 lines of python, create clean and beautiful landing pages with
Splashgen. Don't waste time with no-code tools when you already know how to
code.
"""
site.call_to_action = CTAButton(
    "https://github.com/true3dco/splashgen", "View on GitHub")

launch(site)
