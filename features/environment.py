def before_all(context):
    print("test suite created")

def before_scenario(context, scenario):
    print(f"scenario name is {scenario.name}")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("scenario failed")
    else:
        print("scenario passed")

def before_step(context, step):
    print(f"starting step: {step.name}")

def after_step(context, step):
    if step.status == "failed":
        screenshot_folder = "failed_screenshots"
        context.auto_app.screenshot("failure.png", screenshot_folder)
    print(f"after step: {step.name}")

def after_all(context):
    print("test suite finished")