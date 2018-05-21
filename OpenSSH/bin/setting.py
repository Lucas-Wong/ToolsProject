#! /usr/bin/env python
# _*_coding:utf-8_*_
import re, base64, os, sys, getpass

path = os.path.dirname(os.path.abspath(sys.argv[0]))
'''
选项配置管理
__author__ = 'allen woo'
'''


def add_host_main():
    while 1:
        if add_host():
            break
        print("\n\nAgain:")


def add_host():
    print("================Add=====================")
    print("[Help]Input '#q' exit")
    host_ip = str_format("Host IP:",
                         "^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    if host_ip == "#q":
        return 1

    host_port = str_format("Host port(Default 22):", "[0-9]+")
    if host_port == "#q":
        return 1

    password = str_format("Password:", ".*")
    if password == "#q":
        return 1
    # password = base64.encodestring(password)
    password = base64.encodebytes(password)
    name = str_format("User Name:", "^[^ ]+$")
    if name == "#q":
        return 1
    elif not name:
        os.system("clear")
        print("[Warning]:User name cannot be emptyg")
        return 0

    # The alias
    alias = str_format("Local Alias:", "^[^ ]+$")
    if alias == "#q":
        return 1
    elif not alias:
        os.system("clear")
        print("[Warning]:Alias cannot be emptyg")
        return 0

    of = open("{}/data/information.d".format(path))
    hosts = of.readlines()
    for l in hosts:
        l = l.strip("\n")
        if not l:
            continue
        l_list = l.split(" ")
        if host_ip == l_list[1] and host_port == l_list[2]:
            os.system("clear")
            print("[Warning]{}:{} existing".format(host_ip, host_port))
            return 0
        if alias == l_list[4]:
            os.system("clear")
            print("[Warning]Alias '{}' existing".format(alias))
            return 0

    of.close()

    # save
    of = open("{}/data/information.d".format(path), "a")
    of.write("\n{} {} {} {} {}".format(name.strip("\n"), host_ip.strip("\n"), host_port, password.strip("\n"),
                                       alias.strip("\n")))
    of.close()
    # print("Add the success:{} {}@{}:{}".format(alias.strip("\n"), name.strip("\n"), host_ip.strip("\n"), host_port,
    #                                           password.strip("\n")))
    return 1


def remove_host():
    while 1:

        of = open("{}/data/information.d".format(path))
        hosts = of.readlines()
        of.close
        l = len(hosts)
        if l <= 0:
            os.system("clear")
            print("[Warning]There is no host")
            return

        print("================Remove================")
        print("+{}+".format("-" * 40))
        print("|     Alias   UserName@IP:PORT")
        hosts_temp = []
        n = 0
        for i in range(0, l):
            if not hosts[i].strip():
                continue
            v_list = hosts[i].strip().split(" ")
            print("+{}+".format("-" * 40))
            print("| {} | {}   {}@{}:{}".format(n + 1, v_list[4], v_list[0], v_list[1], v_list[2]))
            n += 1
            hosts_temp.append(hosts[i])
        hosts = hosts_temp[:]
        print("+{}+".format("-" * 40))
        c = input("[Remove]Choose the Number or Alias('#q' to exit):")
        is_alias = False
        is_y = False
        try:
            c = int(c)
            if c > l or c < 1:
                os.system("clear")
                print("[Warning]:There is no")
                continue
            del hosts[c - 1]
            is_y = True

        except:
            is_alias = True
        if is_alias:
            if c.strip() == "#q":
                os.system("clear")
                break

            n = 0
            for l in hosts:
                if c.strip() == l.split(" ")[4].strip():
                    del hosts[n]
                    is_y = True
                n += 1

        if not is_y:
            os.system("clear")
            print("[Warning]:There is no")
            continue
        else:

            # save
            c = input("Remove?[y/n]:")
            if c.strip().upper() == "Y":
                of = open("{}/data/information.d".format(path), "w")
                for l in hosts:
                    of.write(l)
                print("Remove the success！")
                of.close()


def str_format(lable, rule):
    while 1:
        print("{} ('#q' exit)".format(lable))
        if lable.strip().strip(":").upper() == "PASSWORD":
            temp = getpass.getpass()
        else:

            temp = input().strip()
        m = re.match(r"{}".format(rule), temp)
        if m:
            break
        elif "port" in lable:
            temp = 22
            break
        elif temp.strip() == "#q":
            os.system("clear")
            break
        os.system("clear")
        print("[Warning]:Invalid format")

    return temp


def about():
    of = open("{}/data/about.dat".format(path))
    rf = of.read()
    try:
        info = eval(rf)
        os.system("clear")
        print("================About osnssh================")
        for k, v in info.items():
            print("{}: {}".format(k, v))
    except:
        print("For failure.")
    return

