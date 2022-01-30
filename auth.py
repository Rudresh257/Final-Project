login_info = {'Rudresh':'7809',
              'Sibul':'@257',
              'Sanu':'ctc1'}

def log_in(username,password):
    pw = login_info.get(username)
    if pw != password:
        print('Wrong username or password')
        return False
    else:
        return True