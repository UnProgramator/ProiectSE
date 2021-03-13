import SE_core as core
import utils
import SE_web as web



def main():
    web.set_callback(core.callback)
    core.main()
    web.main_loop()

if __name__=="__main__":
    main()
