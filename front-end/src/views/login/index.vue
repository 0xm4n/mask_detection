<template>
  <div class="sign-in-page">
    <div class="placeholder-top"></div>
    <div class="placeholder-bottom">
      <div class="sign-in-box">
        <div class="sign-in-container">
          <div class="container1">
            <img src="./mask.png" alt="Mask" class="logo" />
            <div class="title-container">
              <h2 class="title">Mask Detection</h2>
            </div>
            <form
              ref="loginForm"
              :model="loginForm"
              :rules="loginRules"
              class="login-form"
            >
              <span class="wrapper">
                <input
                  ref="username"
                  v-model="loginForm.username"
                  placeholder="Username"
                  name="username"
                  type="text"
                  tabindex="1"
                  autocomplete="on"
                  class="input"
                />
              </span>

              <div class="error-message-container">
                <p class="error-message"></p>
              </div>

              <span class="wrapper">
                <input
                  :key="passwordType"
                  ref="password"
                  v-model="loginForm.password"
                  :type="passwordType"
                  placeholder="Password"
                  name="password"
                  tabindex="2"
                  autocomplete="on"
                  @keyup.enter.native="handleLogin"
                  class="input"
                />
              </span>

              <div class="error-message-container">
                <p class="error-message"></p>
              </div>

              <button
                class="sign-in-btn"
                :loading="loading"
                type="primary"
                @click.native.prevent="handleLogin"
              >
                <div class="btn-content-container">
                  <span class="btn-content">
                    Sign In
                  </span>
                </div>
              </button>
            </form>
            <div class="reset-passw">
              <a href="/password/reset/" class="reset-link">Forgot Password?</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "admin",
        password: "111111",
      },
      loginRules: {
        username: [{ required: true, trigger: "blur" }],
        password: [{ required: true, trigger: "blur" }],
      },
      passwordType: "password",
      loading: false,
      redirect: undefined,
      otherQuery: {},
    };
  },
};
</script>

<style>
.sign-in-page {
  height: 100%;
  width: 100%;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  min-width: 896px;
  background-image: radial-gradient(
    closest-side at 50% 135%,
    #ffffff 50%,
    #eceff1 100%
  );
}

.sign-in-container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  width: 100%;

  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}

.placeholder-top {
  -webkit-box-flex: 0.618;
  -ms-flex-positive: 0.618;
  flex-grow: 0.618;
}

.placeholder-bottom {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
}

.sign-in-box {
  width: 400px;
  background: white;
  padding: 40px 0 33px 0;
  border-radius: 3px;
  -webkit-box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  border: 1px solid #eeeeee;
  margin: 0 auto;
}

.sign-in-container {
  max-width: 340px;
  margin: 0 auto;
}

.container1 {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
}

.logo {
  height: 77px;
  width: 77px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  border-style: none;
  box-sizing: border-box;
}

.input {
  padding: 8.85px 13px;
  font-size: 14px;
  width: 100%;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  color: #546e7a;
  border: 1px solid #cfd8dc;
  border-radius: 3px;
  font-weight: 300;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
  -webkit-transition: 0.4s all;
  -o-transition: 0.4s all;
  transition: 0.4s all;
}

.login-form {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
}

.wrapper {
  display: inline-block;
  position: relative;
}

.error-message-container {
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}

.error-message {
  color: #c62928;
  font-size: 12px;
  line-height: 18px;
  margin: 10px 0 20px 0;
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
.sign-in-btn {
  padding: 0 13px;
  border: 0;
  color: #ffffff;
  background: transparent;
  height: 40px;
  background: linear-gradient(215deg, #546e7a, #37474f);
}

.btn-content-container {
}

.btn-content {
}

.reset-passw {
  margin-top: 20px;
  color: #bdbdbd;
  text-align: right;
}

.reset-link {
  color: #546e7a;
  font-size: 14px;
  line-height: 20px;
  cursor: pointer;
}
</style>
