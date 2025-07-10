/** @odoo-module **/

import { Component, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class RecaptchaComponent extends Component {
    static template = "auth_recaptcha.recaptcha_script_component";

    setup() {
        onMounted(() => {
            const configElement = document.getElementById("recaptcha-config");
            if (!configElement) return;

            const siteKey = configElement.dataset.sitekey;
            if (!siteKey) return;

            const script = document.createElement("script");
            script.src = `https://www.google.com/recaptcha/api.js?render=${siteKey}`;
            script.async = true;
            script.defer = true;
            script.onload = () => {
                if (typeof grecaptcha !== "undefined") {
                    grecaptcha.ready(() => {
                        grecaptcha.execute(siteKey, { action: "login" }).then((token) => {
                            const input = document.createElement("input");
                            input.type = "hidden";
                            input.name = "g-recaptcha-response";
                            input.value = token;
                            
                            const form = document.querySelector("form.oe_login_form");
                            form.appendChild(input);
                        });
                    });
                }
            };
            document.head.appendChild(script);
        });
    }
}

registry.category("public_components").add("auth_recaptcha.recaptcha_component", RecaptchaComponent);
