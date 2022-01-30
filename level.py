def uploadLevel(rstr, arg1, arg2, name, login):
    endpoint = arg1
    le = str(random.randint(0, 50))
    aa = login.split(",")
    data = {
        'gameVersion': 21,
        'binaryVersion': 35,
        'gdw': 0,
        'accountID': aa[0],
        'gjp': "d1JQSFdfXkdeWUs=",
        'userName': name+" "+rstr, 
        'levelName': "Clown gdps",
        'levelDesc': "R0RQUyB3YXMgc3BhbW1lZCBieSBNSCBUZWFtIGJvdCA=",
        'levelVersion': 666,
        'levelLength': le,
        'audioTrack': 16,
        'auto': 0,
        'password': 2286,
        'original': 0,
        'twoPlayer': 0,
        'songID': 735184,
        'objects': 666,
        'coins': 21474836,
        'requestedStars': 6,
        'unlisted': 0,
        'wt': 11,
        'wt2': 0,
        'ldm': 1,
        'extraString': "0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0",
        'levelString': "H4sIAAAAAAAAA7VcW4_mRA79Q-lWuVxXIR4YxKKVWCRAYhheWgxCsAtPK60Qq_3xW7cklcTH-ZrLw_TXUy67XPbxKSdf0j9_xWmhF_Niyz8u_4herPcvZPsHtw_38kQv4YWMMS_xhV7I1x-pTE8v9L9XqNMfU8-iep3TFfr8GyP2pepLhsjuhm598dCMeY03AZrp23ogLn8gplZZ2VV1y6wvHgQLy88fES8u1U-_UP0Ii6kfbik_---xj4yPVD--4tz-ZxdXfnL7vQk-cs1Kl5LpH7SYD2gpIYyLXZ5sXnih7BcOZa4vgqVNZD9PyyTOeg5F7OtcKnOzoTLVlf8v1s5TbVrYmMVWP4qafeYYiw7XdZJfbNF1IVVvqCr7_Gz9NiYMuetQvA71rRVBWGw0p2EyYJzBeADjWR6vARDHPRhP8jjTPk6xKI-tOr8PuPNAD2MZtiVt-_B5tKe2addl1ny5AwBGErKQGCOMsTAW5rHVF7M5nQu6V80KG1twVT5o-eFtpr9_-vlP7__5xrznr__13cdvzHef_vLfaqXMWnVcjdBTNnVfNNSnhfI5Ot2fwwjvI8blXcvsUfF7xIYBnoRSzXSrc2TDYdq87_rTx1oq2x5ii8G39stfv__tDb_75h8_fs9vfnr_ln759mP3n89-_PDDfSkbQX1GzxTDMZetNk85qrC8jCUhb33iHLxu7jCSjkDr5lgoZBYqmQ-lbAsDrrrULNYVG90MkcOiKIiGjyyXCDt5OEo7ckIBOKEAXBDGshBcZ8TVHcvDQR7Okq9eSLoXku7TNfreb2VGyUjR9FZ0xZ-AkK2poznWtCQqVV7Pp4L7UgjuOoPiOuM0a5gPPb9ms59yrd3gDrVb6oPsUo_DcfyYZ-Mo0ji3FltNGLOrx5M6OVfUQ1EPj6i7Azk8tjqdV-dXrX5RD69Sz2f1_Cp1e957eNXe81k9v0p9bx6CQDDhQDDEvO-yHBjVStnbdLYGmRbCiRZs63TCODqL3bkYuvk42TDNFd9A7blBuuC8YdrvyK-nQbBtUjRibXBblNuM8OyPNZHawbWuAtV93tTPM1YTg1H9Sd3tJdf8E6Tde5tA3R52YG21oTnZZsh2Jl_aaheGOESjgFikkcN-y6Qrz1BruBqj2r5lO4_XjdjsdgfsjrJoehiPMBuy3uyQKGu0Xjo-AZ7DJp8YdQw3Rr1Gs7t5RUyPYowa4pp1p_H1tALI6ORhY3Q5m8MPBTuTL8rJ0GqtkIRWa-useDOrZTlZOfvJg_EExq2MltWaKk2itF9w9QXnXrVeTiz79Rab_VKrnMnTtdpQnTpZ90rV4Kcm-FbVBbOpRn-2NbWv4d7WqN5kdMJLfEt4PcMy4fUsS4S37wQV3lhaobHJhlIawweN6EYUdKIb-xSJrhVE4kfKJuVHyiaTXAY5gnEHxkkrjBxVqVPKJjtcNk-8Nhwlh6ZeXNVdjlsVB3WxdB5XF8tHVe8l1KPbe4x6M2wXuIvgsKBYY-qC5VhKW97qpW89Uy_j_fqV23k11nY7ZLLe-wx85qSBuNdUTzhsf4YJkQ3c7ohy2mV7d3UyZsAz6LDSTS80tiOenCGzFPfD8B729RYR9bsrRq4mMowEAQlA91PW0GqvrKSLgy6We6uO5bGLcl36LFVv3tBMsTUM033Gg4HS7T9LBagZWG8Q9bCUAj5Y8GE6Ilc30zzHPbhKv4U0VuGjha4WjI31vqy_Llla2mep0LUl15t6_X5UrJdMHVt7NUdnd6eo6Per9biEST_1W1ftbtTI3JUWOnes2LIbuFcjBjtx9JO0KQZPOXoQZfa6bMngLa1zw2nNi0jcVPZTrbVlVnm4SFmVZlUagDQ8IEXr8gNSZNmoukbU7QR4wo4sjTM9blNWjiHQ2ROB1p4I9PbFlMpmpHb3xawoHrih_dYdQnF3-BApacIWLFCOfVZE9USh-TABVLWDeoLDtizPlTKSh_SD5EuWVzmY2nEwbmDOMCOrFd3wBUntOWJXwwDdQwoqg6xWzSN2Z-wfXT7rHoMbxJAc5lzhMlePBQ0-WdDhkwUtfjGllodVm_xiVhaPg9qunfZ8UE9HrF0befWInZsrRs0Vo-aKUXPFqLlivblivblivblitbnquzgGbLo0EnoIPnVXw0KW-57HLXgr92eqhX4dtObCXi-R1myIIjNEF1e83FGprqzxduigceigceigcfpB4_SDxskHzVoq3R3Q0671MiY90JKuq3rEFB4xhUdM4XWm8DpTeO1-wPBmvqJvqH9q_FgyHUamiUu8SEKtP377sqL-9RbyCfWPWFiT6G_4zj_MdwefvD3B_yGfRuADYsyAGDMgxgyIMYPOmEFnzKAzZgC3-oc4ogKPqMAjKvCoF3jUCzxqN4qHmxeEj0TmW3QO_TO-X6t_Rve9_mDneL5xPCxesHlvcQ1YQtyUEDclxE1YAE3pbJZ0Nkug73lQLBsfcU06D92nOulU-LABxMb3YEnXO6Gr5Hrz9LAopLoH8JQR02XEdBkx3Z9pCpFm1kkz66SZddL8a42rjGwNYGRrACNbAxi5mNJXUhm5mFXqbLiJGPXptkxWA4DSHzcAOPlhA4iCNQNriAhwsCVAnJYA1RZTajJIZdRiVssV6Zx4GyjSKfFRfcSID-pDcrvPkwWEZC0gJGsBIVkLCKmsoWbIqpxR1tPFOmcw4gxGnMGIM1jnDNY5g1XOYJUzbmHAKmM8qg744kF1xBb3GHSIKxziCoe4wulc4XSucKC9Yhd2d45RjuMJYH42rl3gb480hBKB8rM-ZRfNfK_JelRzHtWcRzXnUc15vea8XnNerzmv3WsaPs1hio2T8vy2QCnbTMevx4bxgCo2oIoNqGKDXpIB3DnZHFHFEaE2ItRGhNqoozbqqI0AtaF9k7eu2u_7xkkvIRgmBMOEYJgQDJMOw6TDMOkwTID6x8bT-oh13Xf9Aj7Owvmbpl06LGeEwYwwmBEGs46irEM0A4iOXXR3SN5id2l8KXDeIhsAXzYAvmwAfIspbQ_FoC5Wr2mZAEqZAEqZAEqZAEoVgQrf4oIuVuFbVv1d4p7dsf0opn6NjYxutgDdbAG62QJ0_7mm1HBYtVCKWV38lxgf0R5B8HIutjdnpFQwqkIsQOXJqDxZLzDWy5P14kbisfnxJk-WQ7O9sCMKoxI3h1jBIVZwiBWcXuNOr3EHanxsoruD9r-91iMKleOLvdXsbi_3zMJ-o2zV5PGC3STwSJDOgtEQ83gTY2r8X9cQ94aRw-W5yXb9UB-lLw1jfdq-XUE4H4PJx-ebctwNNNKzvRNtr-FN4zUG9a2OL7750rx7-_m_z4s3sM2XTg8sfvR-eubU_S4Dh1cPX2eAzpdvafsus16ENXVrYnswce642wuX3N-5mF9uXXHUDSOUBbF6u80YzjaHr_2lAdnXJ83Z9hphf676qTc86YN2ZbGNOnG0n5BpfuJttmR0MevicBGP9x3XCWVDw6cRmOTPgbHG7Bo11uPNo8N4PVzG-AhkN9T4dQQy74Gs2OlX3aW_JH8IpK9-OF6fO9uqhYhHE1t_0vL2k7-9--Lrn97sn598KEz2bfJn9OuP73970x4YamLXj73c369anyU6iCIUtSfMoCwosizIeH1K-jIkrcIbHyARSaK4BgOJLBSRtCHengVGIgNFou_T266iORw4KJFdcHhPDkeCcGhpBToQOdENWs8UIPLYjXrgAVHAHgYcKCsadDBXDmaEcHDpLrh4KcV1ecP93BfR7nDcI47F9nQxCgYWyUVHeC3Ctb8dpGjLYnj3LgNEA5eqHN4uwmUcldrHjCHnK97VCQ6v7CFhDwl76O5EGFGyyGHWcLjIIy6HiLXcXVJEREVclfHmoFEQJW85YvTSTQwTPrkSRlTGzos9wRDhaLQnx6FMOyfx1nSZwkbyek7x0-Gd9yhjYMlRdhhYDifA4Si7G9KRPYwYIqSEmJQwEvaR8M4Ih4pufJSjSHjTpACEFBAQBEG_nyHy3xBJBrtIPEMcY1GATDb-gokikgI8DIoixiJzJxLdMJDJxl9akfDWRSLXjjtJeC2xpeoisStx8_v8Yr6wG2LrMUQYAOJBMZzH4RW7yHG_SlxrveEMJCKsgy6RFwo4tgFvKsDTz21_2wlBV0xxuKkgsU1wjKHLN9CVneebtWTM8A1m5MgbmGIDE8k4uOtLBzAlikhBBtaSq-70asAVNDjHMmUw1mKsFXC2Mk5_xojPOBoZ5zjDTHYluCuFS-T0G92eEj8MNCWNTziNT2JC8p0IkwmGhXySBCzKELjj73tJWkMkZcRb5OC49b9L_g-dLRh98VQAAA==",
        'levelInfo': "gdps spammed lol",
        'secret': "Wmfd2893gb7"
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"/uploadGJLevel21.php", data=data, headers=headers)
    return r.text
