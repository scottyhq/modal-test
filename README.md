# modal-test
experimental with modal

As part of eScience 2025 accelerator, this is a quick attempt to learn about [Modal](https://modal.com) for running remote code on GPU instances. By default Modal runs accross different cloud providers and regions, but you can also specify a specific region and GPU type.

Important: Modal does not run on instances on your cloud account, but rather on Modal's managed infrastructure. They offer limited free tier usage, which is nice for initial testing.

Try it out:

1. first install `pixi` to manage the python environments and setup scripts to run (https://pixi.sh/latest/installation/)

```
gh repo clone scottyhq/modal-test
pixi run setup
```

2. then run some basic test scripts:
```
pixi run
```

