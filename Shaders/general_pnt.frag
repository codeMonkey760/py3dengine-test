#version 460 core

in vec3 posW;
in vec3 normW;
in vec2 texCoord;

layout(location = 0) out vec4 outputColor;

uniform vec3 gCamPos;

struct Light {
    vec3 diffuse;
    vec3 specular;
    vec3 ambient;
    float specPower;
    float intensity;
    vec3 attenuation;
    vec3 position;
};
uniform Light gLights[1];

struct Material {
    sampler2D diffuse;
    vec3 specular;
    vec3 ambient;
};
uniform Material gMaterial;

void main() {
    vec3 normWFixed = normalize(normW);
    vec3 diffuseMaterial = texture(gMaterial.diffuse, texCoord).rgb;

    float distance = distance(gLights[0].position, posW);
    float att = gLights[0].intensity / (gLights[0].attenuation.x + gLights[0].attenuation.y * distance + gLights[0].attenuation.z * distance * distance);

    vec3 toLight = normalize(gLights[0].position - posW);
    float diffuseLight = max(dot(toLight, normWFixed), 0.0f);
    vec4 diffuseColor = vec4((diffuseMaterial * gLights[0].diffuse) * diffuseLight, 1.0f);

    vec3 toEye = normalize(gCamPos - posW);
    vec3 r = reflect(-toLight, normW);
    float t = pow(max(dot(r, toEye), 0.0f), gLights[0].specPower);
    vec4 specColor = vec4((gMaterial.specular * gLights[0].specular) * t, 1.0f);

    vec4 ambientColor = vec4((diffuseMaterial * gMaterial.ambient) * gLights[0].ambient, 1.0f);

    outputColor = ((diffuseColor + specColor) * att) + ambientColor;
}
