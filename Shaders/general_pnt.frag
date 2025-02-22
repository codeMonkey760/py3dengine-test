#version 460 core

in vec3 posW;
in vec3 normW;
in vec2 texCoord;

layout(location = 0) out vec4 outputColor;

uniform vec3 gCamPos;

struct Light {
    int used;
    int enabled;
    int lightType;
    vec3 diffuse;
    vec3 specular;
    vec3 ambient;
    float intensity;
    vec3 attenuation;
    vec3 position;
};
uniform Light gLights[8];

struct Material {
    sampler2D diffuse;
    vec3 specular;
    vec3 ambient;
    float specPower;
};
uniform Material gMaterial;

void main() {
    vec3 normWFixed = normalize(normW);
    vec3 diffuseMaterial = texture(gMaterial.diffuse, texCoord).rgb;

    vec3 finalLightColor = vec3(0.0, 0.0, 0.0);
    for (int curLight = 0; curLight < 8; ++curLight) {
        if (gLights[curLight].used == 0) break;

        if (gLights[curLight].enabled == 0) continue;

        float distance = distance(gLights[curLight].position, posW);
        float att = gLights[curLight].intensity / (gLights[curLight].attenuation.x + gLights[curLight].attenuation.y * distance + gLights[curLight].attenuation.z * distance * distance);

        vec3 toLight = normalize(gLights[curLight].position - posW);
        float diffuseLight = max(dot(toLight, normWFixed), 0.0f);
        vec3 diffuseColor = (diffuseMaterial * gLights[curLight].diffuse) * diffuseLight;

        vec3 toEye = normalize(gCamPos - posW);
        vec3 r = reflect(-toLight, normW);
        float t = pow(max(dot(r, toEye), 0.0f), gMaterial.specPower);
        vec3 specColor = (gMaterial.specular * gLights[curLight].specular) * t;

        vec3 ambientColor = (diffuseMaterial * gMaterial.ambient) * gLights[curLight].ambient;
        finalLightColor += ((diffuseColor + specColor) * att) + ambientColor;
    }

    outputColor = vec4(finalLightColor, 1.0);
}
